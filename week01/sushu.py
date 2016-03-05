for num in range(2, 101):
	count = False
	for x in range(2, num-1):
		if num % x == 0:
			count = True
			break
	if not count:
		print(num)
