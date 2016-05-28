#!/usr/bin/env python
# Gets the number of primes in the list

list1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 29]
# Get prime function .
def get_num(n):
    count = False
    for x in range(2,n-1):
        if n % x == 0:
            count = True
            break
    if not count:
        return n

# Count prime
new_list = []
for i in list1:
    num = get_num(i)
    if num in list1:
        new_list.append(num)
print(len(new_list))