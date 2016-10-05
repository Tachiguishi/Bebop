import urllib
import json

urlDemo = 'http://python-data.dr-chuck.net/comments_42.json'
urlActual = 'http://python-data.dr-chuck.net/comments_248267.json'

jsonString = urllib.urlopen(urlActual).read()

info = json.loads(jsonString)['comments']
numList = []

for item in info:
    numList.append(int(item['count']))

result = sum(numList)
print result
