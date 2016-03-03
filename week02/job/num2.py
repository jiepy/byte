num = 58

lst = list(str(num))

while True:
    if len(lst) >= 2:
        num = 0
        for x in lst:
            num += int(x)
        lst = list(str(num))
    else:
        print(lst)
        break

