import xml.etree.ElementTree as ET
import glob
import codecs
import re


class Parsing:

    def __init__(self):
        self.all_words = set()
        self.songs_lyrics = []

    def all_words_appear(self):
        filenames = glob.glob("../Lyrics/*/*.xml")
        for filename in filenames:
            lyrics = []
            try:
                with codecs.open(filename, "r", "utf8") as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    lgs = root[1][0][0]
                    for lg in lgs:
                        for l in lg:
                            words = l.text.split(' ')
                            if is_hebrew_song(words):
                                # print(words)
                                lyrics.append(l.text)

            except:
                continue
            self.songs_lyrics.append(' '.join(lyrics))
def is_hebrew_song(words):
    for word in words:
        if re.search('[a-zA-Z]', word) == None:  # we want only the Hebrew words
            return True
        with codecs.open("../data/words_to_tag.txt", "a", "utf8") as words_to_tag:
            words_to_tag.write(word + "\n")
    return False
parsing = Parsing()
parsing.all_words_appear()


