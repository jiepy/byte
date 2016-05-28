#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/8 17:42
# ----------------------------------------

# 19
#
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1
#
# 则 19是happy number


def add(num):
	return sum([int(x) ** 2 for x in str(num)])
	# ret = 0
	# for i in str(num):
	# 	ret += (int(i) ** 2)
	# return ret


def happy_num(hnum):
	results = {hnum}
	ret = hnum
	while ret > 10:
		ret = add(ret)
		if ret in results:
			return False
		results.add(ret)
	return ret == 1

for i in range(1, 100):
	if happy_num(i):
		print('{0} is happy num'.format(i))


