from .dbMusic import DbMusic
import xml.etree.ElementTree as ET


class RBox(DbMusic):

    def __init__(self, name):
        super().__init__(name)
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

    def get_all_songs(self):
        return [song for song in self.root.findall('entry') if song.get("type") == 'song']

    def get_aat(self, entry):
        artist = entry.find('artist').text
        album = entry.find('album').text
        track = entry.find('title').text
        return artist, album, track

    def write(self, filename):
        self.tree.write(filename)