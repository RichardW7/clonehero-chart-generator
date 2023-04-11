from flask import Flask, request, redirect, jsonify, send_file, Response
from flask_cors import CORS
from getplaylist import get_playlist
import zipfile 
import io
import base64
import os

app = Flask(__name__)
CORS(app)

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')

SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1'
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

SPOTIFY_SCOPES = 'user-read-private playlist-read-private'

print(SPOTIFY_CLIENT_ID)
print(SPOTIFY_CLIENT_SECRET)
print(SPOTIFY_REDIRECT_URI)

@app.route('/auth')
def auth():
    auth_query_parameters = {
        'response_type': 'code',
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'scope': SPOTIFY_SCOPES,
        'client_id': SPOTIFY_CLIENT_ID
    }
    url_args = '&'.join([f"{key}={value}" for key, value in auth_query_parameters.items()])
    auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
    return jsonify({'url': auth_url})

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    accessToken = data["accessToken"]
    playlistId = data["playlistId"]
    print(f"Access Code: {accessToken}")
    print(f"Playlist ID: {playlistId}")

    if os.path.exists("GeneratedCharts"):
        os.system("rm -r GeneratedCharts")

    os.mkdir("GeneratedCharts")

    buf = io.BytesIO()
    get_playlist(buf, accessToken, playlistId, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI)
    with zipfile.ZipFile(buf, 'w') as zip_file:
        for root, dirs, files in os.walk("GeneratedCharts"):
            for file in files:
                path = os.path.join(root, file)
                zip_file.write(path, os.path.relpath(path, "GeneratedCharts"))
    buf.seek(0)

    os.system("rm -r GeneratedCharts")

    return send_file(buf, mimetype='application/zip', as_attachment=True, download_name='Generated Charts.zip')

@app.route("/")
def hello():
    return Response("Hi from your Flask app running in your Docker container!")

if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)