import extract_data
import process_text
# import Add_Year_To_Json
# import songs_to_years


def main():
    songs_lyrics = extract_data.parsing.songs_lyrics
    print(songs_lyrics)
    filtered_songs = []
    # for song in songs_lyrics:
    #     print(song)
    #     filter = process_text.process_text(song)
    #     if len(filter) != 0:
    #         filtered_songs.append(filter)
    #     print(filtered_songs)
    # print(Add_Year_To_Json)
    # songs_to_years


if __name__ == '__main__':
    main()
