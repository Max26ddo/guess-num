import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	a = input('猜一个数字：')
	a = int(a)
	if a == r:
		print('恭喜你答对了')
		print('这是你猜的第', count, '次')
		break
	elif a > r:
		print('往小里猜')
	elif a < r:
		print('往大里猜')
	print('这是你猜的第', count, '次')