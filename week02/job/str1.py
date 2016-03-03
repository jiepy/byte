#!/usr/bin/env python

str = '12345'



def getnum(x):
    ret = 0
    for i in range(len(x)):
        num = int(str[i])
        ret += num
    return ret
