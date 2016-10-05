import urllib
from bs4 import BeautifulSoup

urlDemo = 'http://python-data.dr-chuck.net/comments_42.html'
urlActual = 'http://python-data.dr-chuck.net/comments_248266.html'
html = urllib.urlopen(urlActual).read()

soup = BeautifulSoup(html, 'html.parser')

listNum = [];
tags = soup('span')
for tag in tags:
    # print 'Contents:',tag.contents[0]
    listNum.append(int(tag.contents[0]))

# print listNum
result = sum(listNum)
print result
