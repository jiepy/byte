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

