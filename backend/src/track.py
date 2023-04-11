import bisect 

class Track:
    def __init__(self, name, id, artist, album, release, duration, img_url, tempo, beats, bars, tatums, sections, segments, time_signature):
        self.name = name
        self.id = id
        self.artist = artist
        self.album = album
        self.year = release[:4]
        self.duration = duration
        self.img_url = img_url
        self.tempo = tempo
        self.beats = self.__initialize_beats(beats)
        self.bars = bars
        self.tatums = tatums
        self.sections = self.__initialize_sections(sections)
        self.time_signature = time_signature
        self.notes = self.__initialize_notes(segments)
        self.frets = self.__initialize_frets(self.notes, self.beats)

    def __initialize_sections(self, sections):
        section_times = {}
        for i in sections:
            info = []
            info.append(i["tempo"])
            info.append(i["time_signature"])
            section_times[i["start"]] = info
        return section_times

    def __initialize_beats(self, beats):
        beat_times = []
        for i in beats:
            beat_times.append(i["start"])
        return beat_times
    
    def __initialize_notes(self, segments):
        notes = []
        index = 0
        for i in segments:
            for j in range(len(i["pitches"])):
                if i["pitches"][j] >= i["pitches"][index]:
                    index = j
            notes.append((str(i["start"]), index, int(i["duration"] * 1000)))
        return notes

    def __initialize_frets(self, notes, beat_times):
        frets = {}
        for note in notes:
            idx = self.__index_of_nearest_beat(beat_times, float(note[0]))
            if beat_times[idx] in frets:
                frets[beat_times[idx]].append((note[1], note[2]))
            else:
                frets[beat_times[idx]] = [(note[1], note[2])]
        return frets
        
    def __index_of_nearest_beat(self, beat_times, note_time):
        idx = bisect.bisect_left(beat_times, note_time)
        if idx == 0:
            return idx
        if idx == len(beat_times):
            return idx - 1
        before = beat_times[idx - 1]
        after = beat_times[idx]
        if after - note_time < note_time - before:
            return idx
        else:
            return idx - 1