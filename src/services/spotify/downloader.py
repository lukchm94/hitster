import json

from .conn import SpotifyWorker

PLAYLIST_LINK: str = (
    "https://open.spotify.com/playlist/3cPuYL23bdF3hS99tXOkSU?si=b94b64391b75438d"
)

PLAYLIST_ID: str = "3cPuYL23bdF3hS99tXOkSU?si=b94b64391b75438d"


def get_spotify_links_from_playlist() -> list[dict]:
    spotify_links: list = []

    spotify_worker = SpotifyWorker().get()

    print(spotify_worker)
    print(spotify_worker)

    print(PLAYLIST_ID)
    results: dict = spotify_worker.playlist_items(PLAYLIST_LINK)
    print(type(results))
    print(len(results.get("items")))
    first_track: dict = results.get("items")[10]
    # print(first_track)
    print(type(first_track))
    print(first_track.keys())
    track: dict = first_track.get("track")
    print(track.keys())
    # return track
    return {
        "preview_url": track.get("preview_url"),
        "external_urls": track.get("external_urls"),
        "artist": track.get("artists"),
        "date": track.get("album").get("release_date"),
    }
    return first_track.get("external_urls")
    return json.load(first_track)
    # print(results)
    # print(results.get(["items"])[0].get("tracks"))
    return results.get(["items"])[0].get("tracks")
    for item in results.get(["items"]):
        print(item)
        # track = item["track"]
        # print(track)
        # track_name = track["name"]
        # track_url = track["external_urls"]["spotify"]
        # print(track_name)
        # print(track_url)
        # spotify_links.append({"track_url": track_url, "track_name": track_name})
        # print(f"{track_name}: {track_url}")

    # return spotify_links
