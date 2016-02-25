#!/usr/bin/env python

list1 = [1, 3, 2, 4, 3, 4, 2, 5, 5, 7]
tmp_list=[]

for i in list1:
	if i in tmp_list:
		continue
	else:
		tmp_list.append(i)

print(tmp_list)
