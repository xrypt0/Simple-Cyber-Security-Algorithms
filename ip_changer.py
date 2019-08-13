import subprocess


ip_address = input(" Your New IP Address : ")


print("IP Changer Started...")

ip = "wlan0"


subprocess.call(["sudo","ifconfig",ip,ip_address])

print("Your IP Address Successfully Changed ! \n \n  \n \n Github Link : https://github.com/wolfnatural ")
