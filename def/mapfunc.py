#!/usr/bin/env python
# ---------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/8
# ---------------------------


def cacl_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax

# result = cacl_sum(1, 2, 3, 4, 5)
#
# print(result)

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum

f = lazy_sum(1, 2, 3, 4, 5)
print(f)