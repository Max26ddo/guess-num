import random
r = random.randint(1, 100)
while True:
	a = input('猜一个数字：')
	a = int(a)
	if a == r:
		print('恭喜你答对了')
		break
	elif a > r:
		print('往小里猜')
	elif a < r:
		print('往大里猜')