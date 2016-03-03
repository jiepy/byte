def getn(num):
    lst = list(str(num))

    while True:
        num_a = 0

        for x in lst:
            num_a += int(x)**2

        if num_a == 1 :
            print('{0} happy: {1}'.format(num, num_a))
            break

        if num_a > 100:
            break
        lst = list(str(num_a))



for i in range(1,10000):
    getn(i)


