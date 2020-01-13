import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT")
print("""


	\033[91mWELCOME TO PORT SCAN\033[0m (DATE: 13/01/2020)

	\033[92m
	1-)Fast Scan
	2-)Service Version İntormation
	3-)İşletim Sistemi Bilgisi

       \033[0m


	""")

operation = input("Please Enter The Number : ")

if(operation == '1'):

	ip = input("Target IP : ")
	os.system("nmap " + ip)

elif(operation == '2'):

	ip = input("Target IP : ")
	os.system("nmap -sS -sV " + ip)

elif(operation == '3'):

	ip = input("Target IP : ")
	os.system("nmap -0 " +ip)

else:
	print("ERROR PLEASE TRY AGAIN")



