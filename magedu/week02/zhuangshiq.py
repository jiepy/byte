import time


def timeit(fn):
	def warp(*args, **kwargs):
		print('----start------')
		ret = fn(*args, **kwargs)
		print('----stop--------')
		return ret

	return warp


# @timeit
def hi(*args, **kwargs):
	for i in args:
		print('* {0}'.format(i))
	for k, v in kwargs.items():
		print('k/v: {0} ---> {1}'.format(k, v))


@timeit
def add(x, y):
	return x + y


a = add(5, 6)

print(a)
# timeit(hi)('a', 'b', 'c', name='topic', email='topic@outlook.com')



# 这样一看似乎很难理解，下面我拆分一下
# hi()函数执行的时候，
# 1. 首先第一步会调用timeit函数,timeit(hi) 此时hi函数作为参数传入了timeit函数，
#    即 tmp = timeit(hi), 可以使用type(tmp)看下返回值是function，即warp函数
#
# 2. 执行warp函数: 首先会打印start,随后执行1步骤中传入的函数,最后再打印stop
#
# 至此，函数执行完毕.
