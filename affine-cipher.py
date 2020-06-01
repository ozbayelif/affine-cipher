import random

def num_to_let(nums):
	lets = []
	for num in nums:
		lets.append(chr(num + 97))
	return lets

def let_to_num(lets):
	nums = []
	for let in lets:
		nums.append(ord(let) - 97)
	return nums

def gen_key(n):
	key = []
	for i in range(n):
		key.append(random.randint(0, 26))
	return key

def enc(m, k):
	mNum = let_to_num(m)
	c = []
	for i in range(len(mNum)):
		c.append((mNum[i] - k[i]) % 26)
	return num_to_let(c)

def dec(c, k):
	cNum = let_to_num(c)
	m = []
	for i in range(len(cNum)):
		m.append((cNum[i] + k[i]) % 26)
	return num_to_let(m)
	
k = gen_key(4)
m = ['d', 'a', 't', 'g']

c = enc(m, k)
print(m)
print(c)
print(dec(c, k))


