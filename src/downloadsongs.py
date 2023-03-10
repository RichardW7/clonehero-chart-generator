from pytube import YouTube
from youtube_search import YoutubeSearch
from datetime import datetime
import constants

def getmp3(track, directory):

    matched = False
    url = ""

    result = YoutubeSearch(track.artist + " " + track.name + " Audio", max_results=20).to_dict()
    for j in result:
        try:
            time = datetime.strptime(j["duration"], "%S")
            total_seconds = time.second
            milliseconds = total_seconds * 1000
        except:
            try:
                time = datetime.strptime(j["duration"], "%M:%S")
                minutes = time.minute
                seconds = time.second
                total_seconds = (minutes * 60) + seconds
                milliseconds = total_seconds * 1000
            except:
                continue
        if milliseconds >= track.duration - 1000 or milliseconds <= track.duration - 1000:
            url = j["url_suffix"]
            matched = True
            break

    if matched == True:
        print("Matched   : " + track.name)
        print("Suffix    : " + url) 
        link = "https://www.youtube.com" + url
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True, mime_type="audio/webm").order_by("abr").desc().first()
        audio.download(constants.CLONE_HERO_PATH + directory, filename = directory + ".mp3")
    else:
        print("Unmatched : " + track.name)
            