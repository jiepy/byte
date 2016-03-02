#!/usr/bin/env python


def fn(x):
    ret = 1
    for i in range(1, x+1):
        ret *= i
        print('i == {0}'.format(i))
        print('ret value:{0}'.format(ret))
        print('-' * 20)
        yield ret

for x in fn(5):
    print('x value: {0}'.format(x))


