import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
api_key=''
serviceurl = 'https://api.themoviedb.org/3/'
# Get name to search
movie = input('Search Movie: ')

parms = dict()
parms['api_key'] = api_key
parms['language'] ='en-US'
parms['query']=movie
url = serviceurl +'search/movie/'+'?'+ urllib.parse.urlencode(parms)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js=json.loads(data)
for item in js['results']:
    print(item['original_title'],' : ',item['release_date'])
