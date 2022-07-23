import extract_data
import process_text
import find_year_of_song
import codecs
import extract_from_shironet


def main():
    songs_lyrics = extract_from_shironet.extract()
    haswords = 0
    total = 0
    withyear = 0
    for song in songs_lyrics:
        total = total + 1
        song_lyrics = song[2]
        song_album = song[1]
        song_singer = song[0]
        print(song_album + "   "+song_singer+ "    ")
        filter_words = process_text.process_text(song_lyrics)
        filter_words = extract_data.remove_vav_and_hei(filter_words)
        # print(song_album+"   "+filter_words)
        if len(filter_words) != 0:
            song_year = find_year_of_song.find_year(song_album, song_singer)
            haswords = haswords + 1
            print("the year of " + song_album + " by " + song_singer + " is " + str(song_year))
            if song_year != 0:
                withyear = withyear + 1
                if int(song_year) < 1980:
                    for word in filter_words:
                        with codecs.open("../words of 1970.txt", "a", "utf8") as words_of_1970:
                            words_of_1970.write(word+"\n")
                if 1980 <= int(song_year) < 1990:
                    for word in filter_words:
                        with codecs.open("../words of 1980.txt", "a", "utf8") as words_of_1980:
                            words_of_1980.write(word+"\n")
                if 1990 <= int(song_year) < 2000:
                    for word in filter_words:
                        with codecs.open("../words of 1990.txt", "a", "utf8") as words_of_1990:
                            words_of_1990.write(word+"\n")
                if 2000 <= int(song_year) < 2010:
                    for word in filter_words:
                        with codecs.open("../words of 2000.txt", "a", "utf8") as words_of_2000:
                            words_of_2000.write(word+"\n")
                if 2010 <= int(song_year):
                    for word in filter_words:
                        with codecs.open("../words of 2010.txt", "a", "utf8") as words_of_2010:
                            words_of_2010.write(word+"\n")
    print(total)
    print(haswords)
    print(withyear)


if __name__ == '__main__':
    main()
