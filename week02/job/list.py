def find(*origin, items=[3, 4]):

	dicta = {}
	lista = []
	for [index, value] in enumerate(origin):

		for i in items:
			if i == value:
				#print('{0} -- {1}'.format(i, index))
				lista.append(index)
		# dicta[i] = index

	print(tuple(lista))



lista = [2, 3, 5, 3, 4, 2, 7, 4]

find(*lista)
