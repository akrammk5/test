#!/usr/bin/env python3
"""Build a compact, real-data XMLTV guide for the SmartOne master M3U.

Source: https://epg.pw/xmltv/epg.xml.gz
Only the source's actual programme entries are included; no schedules are fabricated.
"""
from __future__ import annotations

import collections
import datetime as dt
import gzip
import json
import pathlib
import re
import tempfile
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
PLAYLIST = HERE / "ALL_TV_ONE_PLAYLIST_CLEAN.m3u"
XML_OUT = HERE / "ALL_TV_HD_EPG.xml"
GZIP_OUT = HERE / "ALL_TV_HD_EPG.xml.gz"
SOURCE = "https://epg.pw/xmltv/epg.xml.gz"
NOW = dt.datetime.now(dt.timezone.utc)
EARLIEST = NOW - dt.timedelta(hours=3)
LATEST = NOW + dt.timedelta(hours=48)

# Do not identify unrelated premium packages as these free FAST channels.
ALIASES = {
    "aljazeeraarabic": ["Al Jazeera"],
    "france24arabic": ["France 24 Arabian", "France24 Arabic"],
    "france24french": ["France 24 Francais", "France 24 (French)"],
    "france24english": ["France 24 (English)"],
    "cbssportsgolazo": ["CBS Sports Golazo Network"],
    "france24francais": ["France 24 (French)", "France 24 Francais"],
    "skynewsarabia": ["SkyNewsArabia"],
    "fifaenglish": ["FIFA+"],
    "euronewsfrench": ["Euronews French"],
    "euronewsenglish": ["Euronews English"],
    "dwenglish": ["DW (English)"],
    "tagesschau24": ["tagesschau24"],
    "dasersteard": ["Das Erste"],
    "realdmadrid": ["Real Madrid TV"],
    "africanewsfrench": ["Africanews French"],
}
AMBIGUOUS = {"movies", "sport", "sports", "news", "music", "quran", "sbc", "cna"}

def normalize(text):
    text = unicodedata.normalize("NFKD", str(text)).lower()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", text)

def parse_m3u(path):
    rows = path.read_text(encoding="utf8").splitlines()
    channels = []
    seen = set()
    for line in rows:
        if not line.startswith("#EXTINF:"):
            continue
        match = re.search(r'tvg-id="([^"]+)"', line)
        if not match:
            raise ValueError("Missing tvg-id in master playlist")
        cid = match.group(1)
        name = line.rsplit(",", 1)[-1].strip()
        if cid in seen:
            raise ValueError(f"Duplicate tvg-id: {cid}")
        seen.add(cid)
        channels.append({"id": cid, "name": name})
    if not 100 <= len(channels) <= 300:
        raise ValueError(f"Unexpected master playlist size: {len(channels)}")
    return channels

def parse_time(value):
    if not value or len(value) < 12:
        return None
    digits = value[:14] if len(value) >= 14 else value[:12] + "00"
    try:
        t = dt.datetime.strptime(digits, "%Y%m%d%H%M%S")
        tail = value[14:].strip()
        offset = re.search(r"([+-])(\d{2})(\d{2})", tail)
        if offset:
            amount = int(offset.group(2)) * 60 + int(offset.group(3))
            if offset.group(1) == "-":
                amount *= -1
            return t.replace(tzinfo=dt.timezone(dt.timedelta(minutes=amount))).astimezone(dt.timezone.utc)
        return t.replace(tzinfo=dt.timezone.utc)
    except (ValueError, OverflowError):
        return None

def download_feed():
    request = urllib.request.Request(SOURCE, headers={"User-Agent": "Mozilla/5.0 (compatible; World-TV-HD-EPG/1.0)"})
    with urllib.request.urlopen(request, timeout=100) as response:
        if response.status != 200:
            raise RuntimeError(f"EPG source HTTP {response.status}")
        with tempfile.NamedTemporaryFile(suffix=".xml.gz", delete=False) as tmp:
            path = pathlib.Path(tmp.name)
            total = 0
            while True:
                block = response.read(1024 * 512)
                if not block:
                    break
                total += len(block)
                if total > 100 * 1024 * 1024:
                    raise RuntimeError("EPG source unexpectedly large")
                tmp.write(block)
    print("EPG_DOWNLOAD", total, flush=True)
    return path

def iter_xml(path):
    with gzip.open(path, "rb") as inp:
        events = ET.iterparse(inp, events=("start", "end"))
        root = None
        for event, elem in events:
            if root is None and event == "start":
                root = elem
            if event != "end":
                continue
            tag = elem.tag.rsplit("}", 1)[-1]
            if tag in ("channel", "programme"):
                yield tag, elem
                elem.clear()
                if root is not None:
                    root.clear()

def build():
    channels = parse_m3u(PLAYLIST)
    guide = download_feed()
    # Source IDs explicitly assigned to known channels outrank display-name matching.
    numeric = {x["id"]: x for x in channels if x["id"].isdigit()}
    exact = collections.defaultdict(list)
    for ch in channels:
        key = normalize(ch["name"])
        if len(key) >= 5 and key not in AMBIGUOUS:
            exact[key].append(ch)
        for alias in ALIASES.get(key, []):
            exact[normalize(alias)].append(ch)

    possible = collections.defaultdict(list)
    providers = {}
    programme_bytes = collections.defaultdict(list)
    try:
        for tag, elem in iter_xml(guide):
            if tag == "channel":
                original_id = elem.attrib.get("id", "")
                labels = [c.text.strip() for c in elem.findall("display-name") if c.text]
                providers[original_id] = labels
                if original_id in numeric:
                    possible[original_id].append((numeric[original_id]["id"], 100))
                for label in labels:
                    key = normalize(label)
                    for dest in exact.get(key, []):
                        score = 80 if normalize(dest["name"]) == key else 60
                        possible[original_id].append((dest["id"], score))
                continue

            original_id = elem.attrib.get("channel", "")
            if original_id not in possible:
                continue
            start = parse_time(elem.attrib.get("start", ""))
            end = parse_time(elem.attrib.get("stop", "")) or start
            if start is None or end is None or start > LATEST or end < EARLIEST:
                continue
            programme_bytes[original_id].append(ET.tostring(elem, encoding="utf-8"))
    finally:
        guide.unlink(missing_ok=True)

    # Candidate source with the most current programmes wins for each target.
    options = collections.defaultdict(list)
    for source_id, mappings in possible.items():
        count = len(programme_bytes.get(source_id, []))
        if not count:
            continue
        for destination_id, score in mappings:
            options[destination_id].append((count, score, source_id))

    selected = {}
    used_sources = set()
    for ch in channels:
        choices = sorted(options.get(ch["id"], []), reverse=True)
        for count, score, source_id in choices:
            if source_id not in used_sources:
                selected[ch["id"]] = (source_id, count, score)
                used_sources.add(source_id)
                break

    if len(selected) < 8:
        raise RuntimeError(f"EPG mapping too sparse: {len(selected)} channels. Do not publish an empty guide.")

    # Create valid XMLTV with the exact IDs used by the M3U.
    tv = ET.Element("tv", {
        "generator-info-name": "World TV HD - curated SmartOne guide",
        "source-info-name": "epg.pw",
        "source-info-url": "https://epg.pw/xmltv.html",
    })
    for ch in channels:
        ce = ET.SubElement(tv, "channel", {"id": ch["id"]})
        ET.SubElement(ce, "display-name").text = ch["name"]

    count_programmes = 0
    for ch in channels:
        best = selected.get(ch["id"])
        if not best:
            continue
        src_id, _, _ = best
        for raw in programme_bytes[src_id]:
            elem = ET.fromstring(raw)
            elem.set("channel", ch["id"])
            tv.append(elem)
            count_programmes += 1

    ET.indent(tv, space="  ")
    content = b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(tv, encoding="utf-8") + b"\n"
    if len(content) > 9 * 1024 * 1024:
        raise RuntimeError("Curated guide too large to be reliable on SmartOne")
    # Avoid broken XMLTV after a source outage.
    if count_programmes < 50:
        raise RuntimeError(f"Too few real programmes: {count_programmes}")
    XML_OUT.write_bytes(content)
    with gzip.open(GZIP_OUT, "wb", compresslevel=8) as fout:
        fout.write(content)

    report = {
        "playlist_channels": len(channels),
        "guide_channels_with_real_schedule": len(selected),
        "real_programmes": count_programmes,
        "xml_bytes": XML_OUT.stat().st_size,
        "gz_bytes": GZIP_OUT.stat().st_size,
        "window_utc": [EARLIEST.isoformat(), LATEST.isoformat()],
        "mapped_channels": [ch["name"] for ch in channels if ch["id"] in selected],
        "not_in_source": [ch["name"] for ch in channels if ch["id"] not in selected],
        "source": SOURCE,
    }
    (HERE / "ALL_TV_HD_EPG_STATUS.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf8")
    print("EPG_STATS " + json.dumps({k: v for k, v in report.items() if k not in ("mapped_channels", "not_in_source")}), flush=True)
    print("EPG_MATCHED " + json.dumps(report["mapped_channels"], ensure_ascii=False), flush=True)
    print("EPG_MISSING " + json.dumps(report["not_in_source"], ensure_ascii=False), flush=True)

if __name__ == "__main__":
    build()
