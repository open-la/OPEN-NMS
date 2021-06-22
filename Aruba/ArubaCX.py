import json
import requests
import urllib3
import mysql.connector

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

creds = {"username": "admin", "password": "Gecko#1991"}
print("test")


class ArubaCX_Switch:
    def get_logs(self):
        session = requests.session()

        login = session.post(f"https://{self}/rest/v1/login", data=creds, verify=False)
        print(f"Login code from Switch: {login.status_code}")
        print(f"This is Cookie: {login.cookies}")

        get_log = session.get(f"https://{self}/rest/v1/logs/event?since=today")
        # print(f"Log Line: {get_log.json()}")

        data = get_log.json()

        for i in data['entities']:
            # print(f"Log Processing by Loop:{i}")
            mydb = mysql.connector.connect(
                host="localhost",
                user="dinusha",
                password="Gecko#1991",
                database="open_nms"
            )
            mycursor = mydb.cursor()

            sql = "INSERT INTO log (log_id, log, source) VALUES (%s, %s, %s)"
            val = ("", json.dumps(i), self)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

        logout = session.post(f"https://{self}/rest/v1/logout")
        print(f"Logout Code from Switch:{logout.status_code}")
