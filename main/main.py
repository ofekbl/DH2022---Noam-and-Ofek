import json
import requests
def process_text(text):
    headers = {'Content-Type': 'text/plain;charset=utf-8'}
    params = {
        "task": "nakdan",
        "genre": "modern",
        "data": text,
        "addmorph": True,
        "matchpartial": True,
        "keepmetagim": False,
        "keepqq": False,
    }
    r = requests.post("https://nakdan-4-0.loadbalancer.dicta.org.il/addnikud", headers=headers, json=params)
    r.encoding = "UTF-8"
    # return (r.text)
    x = json.loads(r.text)
    ds = []
    for item in x:
        y = {}
        if ('word' in item) and item['sep'] is False:
            y['word'] = item['word']
        for inner in item['options']:
            y['morph'] = '0x{0:0{1}X}'.format(int(inner['morph']), 16)
        if len(y) > 0:
            ds.append(y)

    return ds

def isFemale(item):
    return item['morph'][12] == '4' or item['morph'][12] == '5'


def isAdj(item):
    return item['morph'][13] == '1'

def filterWords(items):
    out = []
    for i in range(len(items) - 1):
        if isAdj(items[i]) and isFemale(items[i]):
            out.append(items[i]['word'])
    return out

# def speakingAboutNoun(items,i):
#     for

def main() :
    proc = process_text("היא יפה מאוד ונמוכה אבל היא רוצה ללכת לים עם המזוודה הקטנה היפה שלה")
    print(filterWords(proc))

if __name__ == '__main__':
    main()
