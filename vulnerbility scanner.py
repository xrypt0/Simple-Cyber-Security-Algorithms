import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VULNERBILITY SCANNER !") 

print("DATE :  15/01/2020")
	
ip = input("\033[91mPlease Enter The Target IP : \033[0m ")

os.system("nikto -h " +ip)




