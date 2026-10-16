# Algeria SmartOne playlist - audit, 17 October 2026

This M3U URL was originally a 28-entry experiment with **17 entries from a 2021 archive**. Many did not play on the user's Samsung Q8F. The unreliable entries have been removed from the primary playlist.

Main playlist (6 unique candidates):
https://raw.githubusercontent.com/akrammk5/test/main/iptv/Algeria_ALL_28_Test_SmartOne.m3u

The file name is unchanged so the existing SmartOne account can still access it after reloading, but the content is now **6 entries, not 28**. None of the six have been independently playback-tested from Poland. Presence in an upstream directory is not proof that a stream is alive or licensed. Current upstream catalog:
https://github.com/iptv-org/iptv/blob/master/streams/dz.m3u

Two publisher-origin candidates: AL24 News and El Heddaf TV.
Four community-listed but unverified candidates: Amou Yazid TV, CNA, Elwatania TV, TV2.

Excluded: old CDN archive streams, non-HLS TV4 endpoint, duplicate CNA entry, and unrelated Egypt Nile Drama entry.
Echorouk TV, Echorouk News, Ennahar TV, Samira TV, El Bilad TV and El Hayat TV are *not* included in the cleaned playlist because their broadcaster-authorized working direct M3U endpoints could not be verified. Those broadcasters may have official website video players.

The old 28-entry file remains available only for reference:
https://github.com/akrammk5/test/blob/main/iptv/archive/Algeria_28_UNVERIFIED_ARCHIVE.m3u

Separate automatically health-scanned **third-party** option (not personally verified for every stream):
https://dearbulut.github.io/iptv/playlists/country/dz.m3u

Notes:
- A successful HTTP connection to a playlist URL does not prove each HLS video actually plays.
- Some sources may be geo-blocked, fail on SmartOne, use HTTP (not HTTPS), or disappear without notice.
- SmartOne may cache a playlist; reload the account, or restart the app to refresh.
- Do not represent this playlist as guaranteed working, 24/7, or broadcaster-authorized.
