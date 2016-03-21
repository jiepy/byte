#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/16 23:38
# ----------------------------------------


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
	def __init__(self):
		self.top = None

	def push(self, value):
		node = Node(value)
		node.next = self.top
		self.top = node

	def pop(self):
		node = self.top
		self.top = node.next
		return node.value


if __name__ == '__main__':
	stack = Stack()

	# for i in range(10):
	# 	stack.push(i)
	#
	# while stack.top:
	# 	print(stack.pop())
	exp = '{a * [x/(x+y)]}'
	for c in exp:
		if c in '{[(':
			stack.push(c)
		elif c in '}])':
			v = stack.top.value
			if c == '}' and v != '{':
				raise Exception('failed')
			if c == ']' and v != '[':
				raise Exception('failed')
			if c == ')' and v != '(':
				raise Exception('failed')
			stack.pop()

	if stack.top is not None:
		raise Exception('failed')
	print('ok')
