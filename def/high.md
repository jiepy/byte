# 基本函数
# 1. 定义一个， 求 一个数值的平方

def mi2(x):
	return x ** 2

# 将变量f指向函数mi2，则可以使用f变量名称来直接调用mi2函数
# 因为此时变量f已经指向mi2的函数对象
f = mi2

# value = f(5)
# print(value)

# 高阶函数
<<<<<<< HEAD
# 2. 可以接受函数作为参数的函数
#
# 计算两个数值的平方相加
# 此时则可以定义一个函数，直接调用mi2函数求参数的平方然后相加


def add_mi(x, y, func):
	return func(x) + func(y)


# 调用add_mi函数并赋值打印看看
# 例如计算出 5的平方+2的平方

result = add_mi(5, 2, mi2)
print(result)

# 此函数的执行过程是：
# add_mi(5, 2, mi2) ---> mi2(5) + mi2(2) --> 5 ** 2 + 2 **2


# 即add_mi函数参数中接受了mi2函数，则add_mi就是高阶函数.
# 函数作为参数传入，接收函数作为参数的函数称之为 高阶函数
=======
# 2. 可以接受

>>>>>>> origin/master
