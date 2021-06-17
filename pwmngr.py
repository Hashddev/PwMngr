import os.path
import signInInfo
import hashlib
import time
import passWordGen

def checkExistence():
	if os.path.exists("info.txt"):
		pass
	else:
		file = open("info.txt", 'w')
		file.close()

def appendNew():
	file = open("info.txt", 'a')
	userName = input("Please enter the user name: ")
	password = input("Please enter the password here: ")
	website = input("Please enter the website address here: ")
	usrnm = "UserName: " + userName + "\n"
	pwd = "Password: " + password + "\n"
	web = "Website: " + website + "\n"

	file.write("---------------------------------\n")
	file.write(usrnm)
	file.write(pwd)
	file.write(web)
	file.write("---------------------------------\n")
	file.write("\n")
	file.close
	
def readPasswords():
	file = open('info.txt', 'r')
	content = file.read()
	file.close()
	print(content)
	proceed = input("Go back to Main Menu? [Y/n] ")
	if proceed == 'y' or 'Y':
		mainMenu()
	elif proceed == 'n' or 'N':
		print("OK")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print("..")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("Bye ^-^")

		
def mainMenu():
	print("""
	\n\n
	⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀
	⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
	⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀
	⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀
	⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀
	⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀
				* Meow *
	""")
	print("\nHello " + userNameInput + '\n')
	print("""
	[1] Read Passwords
	[2] Add Password
	[3] Generate Password
	[4] Credits
	[5] Quit

	""")
	menuSelect = int(input("What is your option (INT)? "))
	if menuSelect == 1:
		readPasswords()
	elif menuSelect == 2:
		appendNew()
	elif menuSelect == 3:
		genPassWord()
	elif menuSelect == 4:
		credits()
	elif menuSelect == 5:
		checkExistence()

def credits():
	print("""
	\n
	Main Developer: N33dJe5u5
		* Github: https://github.com/N33dJe5u5
	
	Idea: Kalle Halden
		* Video: https://www.youtube.com/watch?v=S4E4yAktjug
	
	Sample Code: Muhimen
		* Github: https://github.com/Muhimen123
		* Article: https://dev.to/muhimen123/make-a-password-manager-with-python-making-the-basic-mechanisms-46im
	""")
		
def signIn():
	global userNameInput, passWordInput
	print("Welcome to PwdMngr by N33dJe5u5\n")
	userNameInput = input("Username: ")
	passWordInput = input("Password: ")
	hashUsrStr = hashlib.md5(userNameInput.encode('utf-8'))
	hashPswStr = hashlib.md5(passWordInput.encode('utf-8'))
	hashdUsr = hashUsrStr.hexdigest()
	hashdPwd = hashPswStr.hexdigest()
	if hashdUsr == signInInfo.userName1:
		if hashdPwd == signInInfo.passWord1:
			mainMenu()
	
def genPassWord():
	passWordGen.generate()
	proceed = input("Go back to Main Menu? [Y/n] ")
	if proceed == 'y' or 'Y':
		mainMenu()
	elif proceed == 'n' or 'N':
		print("OK")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print("..")
		time.sleep(1)
		print("...")
		time.sleep(1)
		print("Bye ^-^")
signIn()
