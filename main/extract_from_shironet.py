import requests
from bs4 import BeautifulSoup


def extract():
    # get_album_page("https://shironet.mako.co.il/artist?lang=1&prfid=1021")
    url = 'https://shironet.mako.co.il/html/indexes/performers/'
    r = requests.get(url, allow_redirects=True)
    open('shironet', 'wb').write(r.content)
    root = bytes.decode(r.content)[152:].split('\n')
    output = []
    i = 0
    for t in root:
        if 'artist?lang=' in t and i < 4:
            i = i + 1
            print(i)
            start = t.find('href') + 6
            end = t.find('title=') - 2
            url = 'https://shironet.mako.co.il' + t[start:end]
            output.append(get_album_page(url))
    return output


def get_album_page(url):
    # get_song_page("https://shironet.mako.co.il/artist?type=disc&lang=1&prfid=1021&discid=412")
    songs_lyrics = []
    r = requests.get(url, allow_redirects=True)
    open('shironet', 'wb').write(r.content)
    root = bytes.decode(r.content).split('\n')
    album_name = ""
    singer_name = ""
    for t in root:
        if 'img align="left" src="' in t:
            start = t.find("title") + 7
            end = t.find(" class") - 1
            name = t[start:end]
            if is_hebrew(name):
                singer_name = name[:name.find('-')]
                album_name = name[name.find('-') + 1:]
                print("singer = " + singer_name)
                print("album name = " + album_name)
        if 'https://shironet.mako.co.il/artist?type=disc' in t:
            start = t.find("content") + 9
            end = t.find(' />') - 1
            songs_lyrics.append([album_name, singer_name, get_song_page(t[start:end])])
    return songs_lyrics


def get_song_page(url):
    # get_lyrics("https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=4558&wrkid=23593")
    songs_lyrics = []
    r = requests.get(url, allow_redirects=True)
    open('shironet', 'wb').write(r.content)
    root = bytes.decode(r.content).split('\n')
    for t in root:
        if 'a class="artist_normal_link_clean" href="/artist?type=lyrics' in t:
            start = t.find('href') + 6
            end = t.find('>') - 1
            url = "https://shironet.mako.co.il" + t[start:end]
            print(url)
            songs_lyrics.append(get_lyrics(url))
    return songs_lyrics


def get_lyrics(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    test = soup.find(itemprop="Lyrics")
    output = ""
    try:
        for t in test.contents[0::2]:
            output = output + t.text + "\n"
        return output
    except:
        return ""


def is_hebrew(s):
    for c in s:
        if 1424 <= ord(c) <= 1514:
            return True
    return False
