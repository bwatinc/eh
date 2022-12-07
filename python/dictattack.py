import hashlib
flag = 0
p_hash = input("Enter MD5 hash")
dictionary = input("Enter dictionary Filename:")
try:
	password_file = open(dictionary, "r")
except:
	print("No file found") 
	quit()
for word in password_file:
	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word.strip()).hexdigest()
	if (digest == p_hash):
		print("password has been found ")
		print("password is: " +word) 
		flag = 1
		break
	if (flag == 0):
		print("No password found") 