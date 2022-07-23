import requests
from bs4 import BeautifulSoup


def extract():
    output = []
    for j in range(20, 21):
        url = 'https://shironet.mako.co.il/html/indexes/performers/heb_'+str(j)+'_popular.html'
        r = requests.get(url, allow_redirects=True)
        open('shironet', 'wb').write(r.content)
        root = bytes.decode(r.content)[152:].split('\n')
    # running on each singer
        for t in root:
            if 'artist?lang=' in t:
                start = t.find('href') + 6
                end = t.find('title=') - 2
                url = 'https://shironet.mako.co.il' + t[start:end]
                albums = get_album_page(url)
                for album in albums:
                    output.append(album)
    return output


def get_album_page(url):
    songs = []
    r = requests.get(url, allow_redirects=True)
    open('shironet', 'wb').write(r.content)
    root = bytes.decode(r.content).split('\n')
    album_name = ""
    singer_name = ""
    # running on each album
    for t in root:
        if 'img align="left" src="' in t:
            start = t.find("title") + 7
            end = t.find(" class") - 1
            name = t[start:end]
            if is_hebrew(name):
                singer_name = name[:name.find('-')]
                album_name = name[name.find('-') + 1:]
        if 'https://shironet.mako.co.il/artist?type=disc' in t:
            start = t.find("content") + 9
            end = t.find(' />') - 1
            songs_lyrics = get_song_page(singer_name, album_name, t[start:end])
            for song in songs_lyrics:
                songs.append(song)
    return songs


def get_song_page(singer, album, url):
    songs_lyrics = []
    r = requests.get(url, allow_redirects=True)
    open('shironet', 'wb').write(r.content)
    root = bytes.decode(r.content).split('\n')
    # runnig on each song in the same album
    for t in root:
        if 'a class="artist_normal_link_clean" href="/artist?type=lyrics' in t:
            start = t.find('href') + 6
            end = t.find('>') - 1
            url = "https://shironet.mako.co.il" + t[start:end]
            songs_lyrics.append([singer, album, get_lyrics(url)])
    return songs_lyrics


def get_lyrics(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    test = soup.find(itemprop="Lyrics")
    output = ""
    try:
        for t in test.contents[0::2]:
            output = output + t.text + " "
        return output.replace('\r', ' ')
    except:
        return ""


def is_hebrew(s):
    for c in s:
        if 1424 <= ord(c) <= 1514:
            return True
    return False
