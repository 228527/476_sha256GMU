import hashlib, binascii

def hashin(text):
	print("input is:", text)
	data = text.encode("utf8")
	sha256hash = hashlib.sha256(data).digest()
	x = binascii.hexlify(sha256hash)
	print("Output is:   ", x)
	return x
	
g = "Your Name" #string of your choosing

i=0
while i < 10000:
	l = []
	g = hashin(g)

	hashin(g)
	i += 1
	if '0' in hashin(g)[0] and '0' in hashin(g)[1] and '0' in hashin(g)[2]:
		l.append(hashin(g))
		break
	else:
		print("not found")
		continue
print(l)
		


#usage: python sha256.py
#it will show all outputs up until it reaches 3 0s in the beginning
