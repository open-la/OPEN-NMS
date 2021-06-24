import json
import requests
import urllib3
import mysql.connector

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

creds = {"username": "admin", "password": "Gecko#1991"}
print("test")


class ArubaCX_Switch:
    def get_logs(self, index=1):
        session = requests.session()

        login = session.post(f"https://{self}/rest/v1/login", data=creds, verify=False)
        print(f"Login code from Switch: {login.status_code}")
        print(f"This is Cookie: {login.cookies}")
        get_log = session.get(f"https://{self}/rest/v1/logs/event?since=today")
        # print(f"Log Line: {get_log.json()}")

        logout = session.post(f"https://{self}/rest/v1/logout")
        print(f"Logout Code from Switch:{logout.status_code}")

        data = get_log.json()
        # print(f"Data from Jason : {data}")

        for i in data['entities']:
            index += 1
            
            print(f"Log Processing by Loop: {index} entity is  {i}")
            mydb = mysql.connector.connect(
                host="localhost",
                user="dinusha",
                password="Gecko#1991",
                database="open_nms"
            )

            mycursor = mydb.cursor()
            time = json.dumps(data['entities'][index]['__REALTIME_TIMESTAMP'])
            message = json.dumps(data['entities'][index]['MESSAGE'])
            sql = "INSERT INTO message (timestamp, message, source_ip) VALUES (%s, %s, %s)"
            val = (time, message, self)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
