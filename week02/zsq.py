def firsh_hi(user='Jie'):
	def say_hi(fn):
		def improve(*args):
			print('-' * 40)
			if 'user' not in args:
				print('no have args')
				print('use default_user: {0}'.format(user))
			return fn(*args)
		return improve
	return say_hi

# @firsh_hi()
def hi(*args):

	for i in args:
		print(i)
	print("End of hi function")


firsh_hi()(hi)('a', 'b', 'c')
#hi('a', 'b', 'c')