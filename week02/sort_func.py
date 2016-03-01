#!/usr/bin/env python


def cmp(x, y):
    return x >= y


def sort(*args):
    ret = []
    for item in args:
        print('*' * 20, item)
        print('-' * 10, ret)
        for i, v in enumerate(ret):
            print('=' * 10, i, v)
            if item >= v:
                ret.insert(i, item)
                break
        else:
            ret.append(item)
    return ret

# s=sort( 3, 1, 2, 5)
# print(s)
# 第一次循环的时候 先进入参数循环 3进去， item为3， 列表ret为空，所以直接执行else语句，则ret=[3]
# 第二次循环的时候 参数1进来，item 为1， ret为3， 里面for循环中，if判断为假，则直接执行else
# 第三次循环的时候 参数2进来， 此时ret为3，1， 会先和index为0的3比较，发现是flase，则和index为1的1比较
# 比1要大，则会执行ret.insert(1, 2) 这样2就插入了1的前面
# 第四次依然5和 index为0的3比较，比3要大，则直接ret.insert(0, 5)

def cmp1(x, y):
    return x >=y


def cmp2(x, y):
    return x <= y


def sort1(cmp, *args):
    ret = []
    for item in args:
        for i, v in enumerate(ret):
            if cmp(item, v):
                ret.insert(i, item)
                break
        else:
            ret.append(item)
    return ret

s1=sort1(cmp1, 3, 1, 2, 5)
print(s1)

s2=sort1(cmp2, 3, 1, 2, 5)
print(s2)