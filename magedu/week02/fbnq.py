#!/usr/bin/env python

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print('n : {0}'.format(n))
        print(b)
        a, b = b, a + b
        n += 1


fab(5)
