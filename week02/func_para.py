#!/usr/bin/env python
#
# ===============================================
# 位置参数说明
# 位置参数 通过参数传递的位置来决定


def echo1(x, y):

	"""
	A function of position Parameter Description
	Args:
		x (int):number
		y (int):number
		return x + y
	"""
	print('x = {0}'.format(x))
	print('y = {0}'.format(y))
	return x + y

# res1 = echo1(2, 6)
# print(res1)

# ===============================================
# 关键字参数
# 关键字参数 通过参数名称来决定
# 同样引用上面定义的函数，这次直接先赋值y值，然后赋值x
# 关键字参数是指直接使用参数名称进行赋值

# res2 = echo1(y=8, x=4)
# print(res2)

# ===============================================
# 混合使用: 关键字 +　位置参数
# 关键字参数必须在位置参数之后

res3 = echo1(10, y=20)
print(res3)

# ===============================================

