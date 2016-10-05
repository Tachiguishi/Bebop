import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

addressDemo = 'South Federal University'
addressActual = 'Saint-Petersburg Polytechnic Univesity'

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': addressActual})
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None
status = js.get('status', 'false')
if status != 'OK':
    print '==== Failure To Retrieve ===='
    print data
    quit()

# print json.dumps(js, indent=4)

placeID = js["results"][0]["place_id"]
print placeID
