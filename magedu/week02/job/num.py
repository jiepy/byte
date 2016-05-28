#!/usr/bin/env python

num = 38
lst = list(str(num))

print(lst)


while True:

    if len(lst) >= 2:
        lst = int(lst[0]) + int(lst[1])
        lst = list(str(lst))
    else:
        print(lst[0])
        break
