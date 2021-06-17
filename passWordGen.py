import random

def generate():
	letterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	rL1 = random.choice(letterList)
	rL2 = random.choice(letterList)
	rL3 = random.choice(letterList)
	rL4 = random.choice(letterList)
	rM1 = str(random.randint(1000, 9999))
	rM2 = str(random.randint(1000, 9999))
	rM3 = str(random.randint(1000, 9999))
	rM4 = str(random.randint(1000, 9999))
	
	print(rL1 + rM1 + '-' + rL2 + rM2 + '-' + rL3 + rM3 + '-' + rL4 + rM4)