# import codecs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import glob
import os
os.environ['SPOTIPY_CLIENT_ID'] = '37a41bb5e05a4e5daa6bfc59f78ce1ed'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'f41d4dd6efc5442f9e298e7cfa381177'


def find_year(song_name,artist_name):
    try:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotify.search(q='track:' + song_name, type='track')
        track_id = results['tracks']['items'][0]['id']
        track_album = spotify.track(track_id)['album']
        album_year = track_album['release_date'][0:4]
        return album_year
    except:
        return 0