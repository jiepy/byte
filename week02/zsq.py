def say_hi(fn):
	def improve():
		print("Welcome from decorator: ")
		fn()
	return improve

@say_hi
def hi():
	print("hi there in hi function")

# hi()

def add(x, y):
	return x+y


a=add(5, 6)

print(a)


