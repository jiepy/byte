from functools import wraps


def get_user(default_user):

	def get_func(fn):
		@wraps(fn)
		def is_have_user(*args, **kwargs):
			if 'user' not in kwargs.keys():
				kwargs['user'] = default_user
			return fn(*args, **kwargs)
		return is_have_user
	return get_func


@get_user(default_user='Jie')
def inuser(*args, **kwargs):
	print(kwargs.get('user'))

# inuser(user='Topic')
inuser()