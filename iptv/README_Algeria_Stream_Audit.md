# Algerian SmartOne IPTV test results (2026-10-17)

This page documents the test performed from a GitHub Actions runner in the United States, not from a Samsung SmartOne TV in Poland.

## Current user playlist: 5 stream candidates that delivered H.264 video

Keep this URL in SmartOne:
https://raw.githubusercontent.com/akrammk5/test/main/iptv/Algeria_ALL_28_Test_SmartOne.m3u

Despite the historical filename (28), the file now has **five entries**:
- AL24 News — HLS media bytes received; ffprobe identified H.264 video.
- El Heddaf TV — HLS media bytes received; ffprobe identified H.264 video.
- Amou Yazid TV — HLS media bytes received; ffprobe identified H.264 video.
- TV2 Algeria — ffprobe identified H.264 video, but the separate HLS media test intermittently returned 404; reliability is uncertain.
- StoryChannel TV — HLS media bytes received; ffprobe identified H.264 video.

Evidence:
- Media checks: https://github.com/akrammk5/test/actions/runs/38981923626
- Codec check: https://github.com/akrammk5/test/actions/runs/38982061560

## Excluded from current playlist

- Echorouk TV, Echorouk News, Ennahar TV and El Bilad TV: tested third-party stream candidates returned HTTP 403.
- CNA and its alternate: HTTP 403.
- Elwatania TV: timed out or failed SSL hostname verification.

The above failures are results for specific URLs tested from the US, not proof that those broadcasters' official websites are unavailable everywhere.

Older unverified 28-entry playlist archived:
https://github.com/akrammk5/test/blob/main/iptv/archive/Algeria_28_UNVERIFIED_ARCHIVE.m3u

This technical test confirms media/codec retrieval **only**. It is not legal-rights verification, continuous uptime monitoring, or a guarantee of playback on Samsung SmartOne in Poland. Individual sources may be geoblocked or break later; check publisher permissions for each stream.
