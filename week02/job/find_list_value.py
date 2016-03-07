# find函数，传入两个列表，其中origin和items,
# tems具有默认值[3,4],查找items中每个元素在origin中的所有位置，返回值为字典，
# key是items中的元素，value是位置的元祖
# 例如: find([2, 3, 5, 3, 4, 2, 7, 4]) 返回{3:(1,3), 4:(4, 7)}


def find(*origin, items=[3, 4]):
	dicta = {}

	for i in items:
		listb = []

		for index, value in enumerate(origin):
			if i == value:
				listb.append(index)
		dicta[i] = tuple(listb)
	print(dicta)

lista = [2, 3, 5, 3, 4, 2, 7, 4]
find(*lista)

