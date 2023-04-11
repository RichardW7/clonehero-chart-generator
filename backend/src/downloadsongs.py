from datetime import datetime
from youtube_search import YoutubeSearch
import yt_dlp

def getogg(track, song_name) -> bool:

    matched = False
    url = ""

    results = YoutubeSearch(song_name + " Audio", max_results=20).to_dict()
    for j in results:
        try:
            duration = j["duration"]
            time = datetime.strptime(duration, "%M:%S")
            total_ms = time.minute * 60 + time.second
            total_ms *= 1000
        except:
            continue

        if abs(total_ms - track.duration) <= 1000:
            url = j["url_suffix"]
            matched = True
            break

    if matched:
        print("Matched   : " + track.name)
        print("Suffix    : " + url) 
        link = "https://www.youtube.com" + url
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': song_name + ".%(ext)s",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'vorbis',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return True
    else:
        print("Unmatched : " + track.name)
        return False
