import urllib
from bs4 import BeautifulSoup

# url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Roger.html'
count = 7
start = 0
position = 17

while start < count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag  = tags[position]
    url  = tag.get('href', None)
    print url
    print 'Name:',tag.contents[0]
    start += 1
