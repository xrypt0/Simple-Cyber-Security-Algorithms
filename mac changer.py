import subprocess


mac_address = input(" Your New MAC Address : ")


print("MAC Changer Started...")

interface = "eth0"


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])

print("Your MAC Address Successfully Changed ! \n \n \n \n Github Link : https://github.com/wolfnatural ")







