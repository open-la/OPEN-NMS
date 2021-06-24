import json

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="dinusha",
    password="Gecko#1991",
    database="open_nms"
)
get_count_cursor = mydb.cursor()

sql_get_log = "SELECT * FROM 'log'"
sql_get_row_count = "SELECT COUNT(*) FROM log"
get_count_cursor.execute(sql_get_row_count)
row_count = get_count_cursor.fetchall()
print(f"Row Count is: {row_count}")


# read lof file in first row
class process_data:
    for i in row_count:
        sql_get_log = "SELECT 'Log' FROM `log` LIMIT 1"
        get_log_cursor = mydb.cursor()
        get_log_value = get_log_cursor.fetchall()
        json_log = get_log_value.json()
        message_content = json_log.dumps('MESSAGE')
        timestamp = json_log.dumps('__REALTIME_TIMESTAMP')

        sql_store_message = "INSERT INTO `message`(`timestamp`, `message`) VALUES(%s, %s)"
        store_log_cursor = mydb.cursor()
        message_val = (timestamp, message_content)
        store_log_cursor.execute(sql_store_message, )

# get each value to variable


# insert value to relevent db
