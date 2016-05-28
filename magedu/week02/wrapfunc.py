#!/usr/bin/env python
# ---------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/8
# ---------------------------

# test.__doc__ 得到函数的文档
#
#
# test.__name__ 得到函数的名称


from functools import wraps


def check(allows):
	def demo(fn):
		@wraps(fn)
		def warp(username, *args, **kwargs):

			if username in allows:
				print('Now in warp function')
				return fn(username, *args, **kwargs)
			return 'not allow'

		return warp

	return demo


@check(['jie', 'topic'])
def test(username):
	'''This is test'''
	print('Test ING .... ')
	return 'Test End ... bye'

# print(test.__name__)
# print(test('jie'))
print(help(test))
# print(test.__doc__)
# print('-' * 20)
# print(test.__name__)