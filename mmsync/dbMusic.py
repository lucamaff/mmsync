import xml.etree.ElementTree as ET


class DbMusic:

    def __init__(self, name):
        self.filename = name

    def get_all_songs(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_aat(self, entry):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_rating(self, entry):
        return entry.find('rating')

    def get_playcount(self, entry):
        return entry.find('play-count')

    def add_rating(self, entry, value):
        rating = ET.Element('rating')
        rating.text = value
        entry.append(rating)

    def add_playcount(self, entry, value):
        playcount = ET.Element('play-count')
        playcount.text = value
        entry.append(playcount)
