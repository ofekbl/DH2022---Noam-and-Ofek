import extract_data
import process_text
import find_year_of_song


def main():
    songs_lyrics = extract_data.parsing.songs_lyrics
    filtered_songs = []
    i = -1
    for song in songs_lyrics:
        song_lyrics = song[2]
        song_name = song[0]
        song_artist = song[1]
        print(song[0])
        filter_words = process_text.process_text(song_lyrics)
        if len(filter_words) != 0:
            song_year = find_year_of_song.find_year(song_name,song_artist)
            filtered_songs.append([song_name,song_year,filter_words])
            i = i+1
            print(filtered_songs[i])

if __name__ == '__main__':
    main()
