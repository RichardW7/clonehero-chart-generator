def ini(track, sourceFile):
    print("[Song]", file = sourceFile)
    print("name = " + track.name, file = sourceFile)
    print("artist = " + track.artist, file = sourceFile)
    print("album = " + track.album, file = sourceFile)
    print("genre = Unknown Genre", file = sourceFile)
    print("year = " + track.year, file = sourceFile)
    # print("song_length = " + track.duration, file = sourceFile)
    print("charter = RichardW", file = sourceFile)
    print("diff_guitar = -1", file = sourceFile)
    print("diff_bass = -1", file = sourceFile)
    print("diff_drums = -1", file = sourceFile)
    print("diff_drums_real = -1", file = sourceFile)
    print("preview_start_time = 0", file = sourceFile)
    print("loading_phrase = \"This song was generated using python\"", file = sourceFile)

