import os
import urllib.request
from createinifile import ini
from createchartfile import chart
from downloadsongs import getogg

def folder(track, buf):

    song_name = track.artist + " - " + track.name
    directory = "GeneratedCharts/" + track.artist + " - " + track.name

    if os.path.exists(directory):
        os.system("rm -r \"" + directory + "\"")

    os.mkdir(directory)

    can_proceed = getogg(track, song_name)

    if can_proceed:
        imgURL = track.img_url["url"]
        urllib.request.urlretrieve(imgURL, directory + "/album.png")
        os.system("mv \"" + song_name + ".ogg\" \"" + directory + "\"/song.ogg")

        sourceFile = open("song.ini", "w")
        ini(track, sourceFile)
        sourceFile.close()

        os.system("mv song.ini \"" + directory + "\"/song.ini")

        sourceFile = open("notes.chart", "w")
        chart(track, sourceFile)
        sourceFile.close()

        os.system("mv notes.chart \"" + directory + "\"/notes.chart")

    