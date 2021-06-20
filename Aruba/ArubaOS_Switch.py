import requests
import pprint

url_vlan = 'http://172.16.20.102/rest/v1/vlans'
url_login = "http://172.16.20.102/rest/v1/login-sessions"

payload_login = "{\"userName\": \"admin\", \"password\": \"plexus@2019\"}"

get_cookie = requests.request("POST", url_login, data=payload_login)
r_cookie = get_cookie.json()['cookie']
headers = {'cookie': r_cookie}


get_vlan = requests.request("GET", url_vlan, payload=headers)
print(get_vlan.text)