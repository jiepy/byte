class A:
	def __init__(self):
		"""

		:rtype: return val
		"""
		self.val = 123


# a = A()
# print(a.val)


class B:
	def __init__(self):
		self.__var = 666

	@property
	def var(self):
		print('get var')
		if self.__var < 0:
			return 0
		return self.__var

	@var.setter
	def var(self, value):
		print('set var')
		if isinstance(value, (int, float)) and value >= 0:
			self.__var = value
			print(value)
		else:
			self.__var = 0


b = B()
b.var = 888
