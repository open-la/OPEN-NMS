import requests
r = requests.get('http://api.zippopotam.us/us/ma/belmont')
j = r.json()

print (j['state'])
print (j['places'][1]['post code'])