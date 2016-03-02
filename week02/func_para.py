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

# res3 = echo1(10, y=20)
# print(res3)

# ===============================================

# 可变参数
# 可变位置参数


def sumn(list1):
    res = 0
    for x in list1:
        res += x
        print(x)
    print(res)


# sumn([1, 2, 3, 4])
# sumn([4, 3, 2, 1])

def func_change(*args):
    res = 0
    print(args)
    for x in args:
        res += x
    print(res)


# func_change(1, 2, 3, 4, 5)

# ===============================================
# 默认参数
# 当默认参数和关键字参数一起使用的时候，世界都是美好的
# 默认参数必须在关键字参数之后


def func_default(x, y=10):
    print('x/y is {0}/{1}'.format(x, y))


# func_default(20)


# ===============================================
#  可变关键字参数


def print_args(**kwargs):
    for k, v in kwargs.items():
        print('key: {0} ===> value : {1}'.format(k, v))


# print_args(x=100, y=200, z=300)

# 可变参数函数在定义的时候，就决定了参数是位置参数还是关键字参数


def print_all(*args, **kwargs):
    for x in args:
        print('POS:{0}'.format(x))
    for k, v in kwargs.items():
        print('Key: {0} ==> Valus: {1}'.format(k, v))


# print_all(1, 2, 3, a=4, b=5)


def print_he(x, y, *args, **kwargs):
    print('x = {0}'.format(x))
    print('y = {0}'.format(y))
    for i in args:
        print('args: x = {0}'.format(i))
    for k, v in kwargs.items():
        print('{0} => {1}'.format(k, v))


# print_he([1,2,3],4, 5,6,7, kk =5)

# 参数传入规则：
# 非默认非可变参数， 可变位置参数，可变关键字参数
# 默认参数不要和可变参数放到一起

# 参数解包


def add(x, y):
    print('x is {0}'.format(x))
    print('y is {0}'.format(y))
    print('Count x + y = {0}'.format(x + y))


# lst = [1, 2]
# add(lst[0], lst[1])
# add(*lst)

# 字典参数传入，函数解包


def func_dict(**kwargs):
    for k, v in kwargs.items():
        print('Key: {0} --> {1}'.format(k, v))


# dict1 = {'a':1, 'b':2, 'c':3}
# func_dict(**dict1)

# 默认参数的坑


def fn(lst=[]):
    lst.append(1)
    print(lst)


# fn()
# 执行完成后lst指向会变成1
# fn()
# 这次执行时候lst=[1]会覆盖默认值[]
# 此次返回[1, 1]
# fn()
# 这次执行时候lst=[1, 1]会覆盖默认值[]
# 此次返回[1, 1, 1]

#  解决方案

# 先给lst赋值为None,判断lst如果是None
# 则新创建列表,然后再append
# 如果lst在调用函数的时候填写了默认值，


def fn1(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    print(lst)
