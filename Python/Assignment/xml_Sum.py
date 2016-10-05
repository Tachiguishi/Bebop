import urllib
import xml.etree.ElementTree as ET

urlDemo = 'http://python-data.dr-chuck.net/comments_42.xml'
urlActual = 'http://python-data.dr-chuck.net/comments_248263.xml'

data = urllib.urlopen(urlActual).read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

numlist = []
numbers = tree.findall('.//count')
for number in numbers:
    print number.text
    numlist.append(int(number.text))

result = sum(numlist)
print result
