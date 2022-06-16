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
        "keepmetagim": True,
        "keepqq": True,
    }
    r = requests.post("https://nakdan-4-0.loadbalancer.dicta.org.il/addnikud", headers=headers, json=params)
    r.encoding = "UTF-8"
    # return (r.text)
    x = json.loads(r.text)
    ds = []
    for item in x:
        y = {}
    #     if item['sep'] == False :
    #         ds.append(item['word'])
        # if (('word' in item) and item['sep'] == False) or (
        #         ('word' in item) and item['word'] == '!' and item['sep'] == True):
        #     y['word'] = item['word']
        #     if item['word'] == '!':
        #         y['morph'] = '0x{0:0{1}X}'.format(int(0), 16)
        # for inner in item['options']:
        #     y['morph'] = '0x{0:0{1}X}'.format(int(inner['morph']), 16)
        # if len(y) > 0:
        #     ds.append(y)

    # return ds

def main() :
    print(0x0000000000200000)
    print(process_text("אהלן, מה נשמע? מה שלומך, איך את?"))

if __name__ == '__main__':
    main()
