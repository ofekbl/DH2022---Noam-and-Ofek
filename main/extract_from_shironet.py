from xml.dom.minidom import parseString

import requests
import html
# import urllib2

def extract():
    # print("in")
    get_album_page("https://shironet.mako.co.il/artist?lang=1&prfid=1021")
    # url = 'https://shironet.mako.co.il/html/indexes/performers/'
    # r = requests.get(url, allow_redirects=True)
    # open('shironet', 'wb').write(r.content)
    # root = bytes.decode(r.content)[152:].split('\n')
    # for t in root:
    #     if 'artist?lang=' in t:
    #         start = t.find('href')+6
    #         end = t.find('title=')-2
    #         url = 'https://shironet.mako.co.il'+t[start:end]
    #         get_album_page(url)
    print("out")


def get_album_page(url):
    get_song_page("https://shironet.mako.co.il/artist?type=disc&lang=1&prfid=1021&discid=412")
    # songs_lyrics = []
    # r = requests.get(url, allow_redirects=True)
    # open('shironet', 'wb').write(r.content)
    # root = bytes.decode(r.content).split('\n')
    # album_name = ""
    # for t in root:
    #     if 'img align="left" src="' in t:
    #         start = t.find("title")+7
    #         end = t.find(" class")-1
    #         name = t[start:end]
    #         singer_name = name[:name.find('-')]
    #         album_name = name[name.find('-')+1:]
    #         print("singer = "+singer_name)
    #         print("album name = "+album_name)
    #     if 'https://shironet.mako.co.il/artist?type=disc' in t:
    #         start = t.find("content")+9
    #         end = t.find(' />')-1
    #         songs_lyrics.append([album_name,singer_name, get_song_page(t[start:end])])
#


def get_song_page(url):
    get_lyrics("https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=4558&wrkid=23593")
    # songs_lyrics = []
    # r = requests.get(url, allow_redirects=True)
    # open('shironet', 'wb').write(r.content)
    # root = bytes.decode(r.content).split('\n')
    # for t in root:
    #     if 'a class="artist_normal_link_clean" href="/artist?type=lyrics' in t:
    #         start = t.find('href')+6
    #         end = t.find('>')-1
    #         url = "https://shironet.mako.co.il"+t[start:end]
    #         print(url)
            # songs_lyrics.append(get_lyrics(url))


def get_lyrics(url):
    from urllib.request import urlopen
    file = urlopen('https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=1021&wrkid=609')
    data = file.read()
    file.close()
    print(data)
    # dom = parseString(data)
    # print(dom)
    # ! /usr/bin/env python
    #
    # try:
    #     # For Python 3.0 and later
    #     from urllib.request import urlopen
    # except : return 0
    #
    # html = urlopen("https://shironet.mako.co.il/artist?type=lyrics&lang=1&prfid=1021&wrkid=609")
    # print(bytes.decode(html.read()))
    # r = requests.get(url, allow_redirects=True)
    # open('shironet', 'wb').write(r.content)
    # root = bytes.decode(r.content)
    # print(r.content[26104:])
    #
    # rrr = r.content[26104:26052+561]
    # print(rrr.decode('UTF-8'))
    # for t in root:
    #     print(t)