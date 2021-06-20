import requests

url_vlan = 'http://192.168.11.254/rest/v1/vlans'
url_login = "http://192.168.11.254s/rest/v1/login-sessions"

payload_login = '{"userName": "admin", "password": "Gecko#1991"}'

get_cookie = requests.request("POST", url_login, data=payload_login)
r_cookie = get_cookie.json()['cookie']
headers = {'cookie': r_cookie}

get_vlan = requests.request("GET", url_vlan, payload=headers)
print(get_vlan.text)
