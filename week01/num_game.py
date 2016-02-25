#!/usr/bin/env python

Luck_num = 10
count = 0

print('Warning: A total of three chances .')
while True:
	input_num = int(input('Please Input Lucky Numbers: '))
	if input_num == Luck_num:
		print('Congratulations! You Win!')
		break
	else:
		count += 1
		if count > 2:
			print('Oops! You Fail!')
			break