import requests
import webbrowser
from urllib.parse import urlencode
import base64

AUTH_URL = 'https://accounts.spotify.com/api/token'

def authenticate (accessToken, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI):

    auth_headers = {
        "client_id": SPOTIFY_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": SPOTIFY_REDIRECT_URI,
        "scope": "user-library-read user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private" 
    }

    encoded_credentials = base64.b64encode(SPOTIFY_CLIENT_ID.encode() + b':' + SPOTIFY_CLIENT_SECRET.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": accessToken,
        "redirect_uri": SPOTIFY_REDIRECT_URI
    }

    r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

    token = r.json()["access_token"]
    
    return token

