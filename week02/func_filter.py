#!/usr/bin/env python


def bigger_5(x):
	if x > 5:
		return True
	return False


for i in range(10):
	if bigger_5(i):
		print(i)

# name = 1
# print('{0:_^11} is a 11 length. '.format(name))
print('-' * 20)
big5_list = list(filter(bigger_5, range(10)))
print(big5_list)
