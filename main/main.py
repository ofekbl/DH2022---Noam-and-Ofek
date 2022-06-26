import extract_data
import process_text


def main():
    # print(process_text.process_text(" סירה חדשה "))
    songs_lyrics = extract_data.parsing.songs_lyrics
    filtered_songs = []
    for song in songs_lyrics:
        print(song)
        filter = process_text.process_text(song)
        if len(filter) != 0:
            filtered_songs.append(filter)
        print(filtered_songs)



if __name__ == '__main__':
    main()
