from .dbMusic import DbMusic
import plistlib
from collections import namedtuple


class iTun(DbMusic):

    def __init__(self, name):
        super().__init__(name)
        with open(self.filename, 'rb') as fp:
            self.dictionary = plistlib.load(fp)['Tracks']
            self.rating_el_struct = namedtuple("rating_el", "text")
            self.playcount_el_struct = namedtuple("playcount_el", "text")

    def get_all_songs(self):
        return [song for song in self.dictionary.values() if 'Album' in song]

    def get_aat(self, entry):
        artist = entry['Artist']
        album = entry['Album']
        track = entry['Name']
        return artist, album, track

    def get_rating(self, entry):
        if 'Rating' in entry and 'Rating Computed' not in entry:
            rating = int(entry['Rating']) // 20
        else:
            rating = 0
        rating_el = self.rating_el_struct(text=str(rating))
        return rating_el

    def get_playcount(self, entry):
        if 'Play Count' in entry:
            playcount = int(entry['Play Count'])
        else:
            playcount = 0
        playcount_el = self.playcount_el_struct(text=str(playcount))
        return playcount_el

    def add_rating(self, entry, value):
        raise NotImplementedError("iTunes class can not be modified")

    def add_playcount(self, entry, value):
        raise NotImplementedError("iTunes class can not be modified")