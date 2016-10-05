import urllib
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_42.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    # print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
