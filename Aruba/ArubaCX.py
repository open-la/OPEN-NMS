import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ip_add = "192.168.11.254"
creds = {"username": "admin",  "password": "Gecko#1991" }

session = requests.session()
login = session.post("https://192.168.11.254/rest/v1/login", data=creds, verify=False)
print(f"Login code from Switch: {login.status_code}")
print(f"This is Cookie: {login.cookies}")
logout = session.post("https://192.168.11.254/rest/v1/logout")
print(f"Logout Code from Switch:{logout.status_code}")
