from Aruba.ArubaCX import *

ip_add = "192.168.11.254"
# get logs from Switch and Store in to DB
ArubaCX_Switch.get_logs(ip_add)
