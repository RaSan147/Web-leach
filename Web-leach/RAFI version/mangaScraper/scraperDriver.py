def init(text):
	string = "?!;:'\"^=[]\*_/`{},<£¢¥≥»≤«~>.@#$%&-+() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789¶∆×÷Π•|"
	alpha =['\n','\t'] + [s for s in string] 
	n = len(alpha)
	t = [c for c in text]
	p = t.pop()
	#print(text[265:275])
	decrypted = []
	for char in t:
		a = alpha.index(char)-int(p)-1
		#print(char)
		if a >= 0:
			decrypted.append(alpha[a])
		elif a < 0:
			b = a-int(p)+n
			decrypted.append(alpha[b])
	return ''.join(decrypted)

# def fuckoff(t):
# 	alpha = "\n\t?!;:'\"^=[]\*_/`{},<£¢¥≥»≤«~>.@#$%&-+() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789¶∆×÷Π•|"
# 	# alpha =['\n','\t'] + [s for s in string] 
# 	n = 110 #len(alpha)
# 	#print(len(alpha))
# 	#t = [c for c in text]
# 	p = int(t.pop)

# 	decrypted=[]
# 	for c in t:
# 		decrypted.append(alpha[(alpha.index(c)-p-1)%n])
	
# 	return ''.join(decrypted)




with open('./resources.dm','r') as f:
	res=f.read()
	print(init(res))
	# appDriver = init(f.read())

# # exec(appDriver)
# import time

# rafi_test=time.time()
# for _ in range(500):
# 	init(res)
# print("rafi: ", time.time()-rafi_test)

# ray_test=time.time()
# for _ in range(500):
# 	init(res)
# print("ray: ", time.time()-ray_test)



	
