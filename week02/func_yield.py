#!/usr/bin/env python


def fn(x):
    ret = 1
    for i in range(1, x+1):
        ret *= i
        print('i == {0}'.format(i))
        print('ret value:{0}'.format(ret))
        yield ret
for x in fn(5):
    print('x value: {0}'.format(x))
    print('-' * 20)

'''
# 程序执行后，for语句进入fn函数并且传入fn为5的参数
# fn 参数中的for循环则循环 1，6，会循环5次
第一次循环 ret = 1 , i = 1, 则 1 * 1 = 1 yield返回值为1
则x的值为1
i == 1
ret value:1
x value: 1
--------------------
因函数fn里的for循环为执行完成，所以for循环则会再次调用fn函数，
因为yield保存了函数执行的现场，则此次i = 2, ret =2 , 1 * 2 =2
i == 2
ret value:2
x value: 2
--------------------
第三次 i = 3 ,ret = 2 * 3 , ret = 6, yield返回ret值给for，则x = 6
第四次 i = 4 ,ret = 6 * 4 , ret = 24, yield返回ret值给for，则x = 24
第五次 i = 5 ,ret = 24 * 5 , ret = 120, yield返回ret值给for，则x = 120
--------------------
'''