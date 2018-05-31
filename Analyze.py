import ast
import json

myNewfile = open("DataFest.csv", "r")
noRetweets = open("noRetweets.txt", "a")
textExists = True
keyExists = False
for dictionary in myNewfile:
    if ( len(dictionary) != 1 ):
        keyExists = False
        textExists = False
        d = json.loads(dictionary, encoding='utf-8')
        for key in d.keys():
            if (key == 'retweeted_status'):
                keyExists = True
            if (key == 'text'):
                textExists = True
        if (textExists):
            print(d['text'])
            text = (str(d['text'].encode('ascii', 'ignore')))
            noRetweets.write(text)
            noRetweets.write("\n")