import requests
from track import Track
from createchartfolder import folder
from gettoken import authenticate
import zipfile
import io

BASE_URL = "https://api.spotify.com/v1/"

def get_playlist(buf, accessToken, PLAYLIST_ID, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI):

    token = authenticate(accessToken, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)

    track_info = requests.get(BASE_URL + "playlists/" + PLAYLIST_ID, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }).json()

    tracks = {}

    print(f"Bearer Token: {token}")

    for track in track_info["tracks"]["items"]:
        #make analysis call
        track_analysis = requests.get(BASE_URL + "audio-analysis/" + track["track"]["id"], headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
        }).json()
        #declare object
        tracks[track["track"]["name"]] = Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"],
        track["track"]["album"]["name"], track["track"]["album"]["release_date"], track["track"]["duration_ms"], 
        track["track"]["album"]["images"][0], track_analysis["track"]["tempo"], track_analysis["beats"],
        track_analysis["bars"], track_analysis["tatums"], track_analysis["sections"], track_analysis["segments"], track_analysis["track"]["time_signature"])

    for i in tracks:
        folder(tracks[i], buf)

