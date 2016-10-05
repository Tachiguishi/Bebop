import urllib
from bs4 import BeautifulSoup

# url = 'http://www.py4inf.com/code/romeo.txt'
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for tag in tags:
    print tag
    print tag.get('href', None)

# print tags
