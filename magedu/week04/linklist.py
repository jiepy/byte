#!/usr/bin/env python
# ---------------------------------------
# author : Geng Jie
# email  : gengjie@outlook.com
#
# Create Time: 2016/3/16 22:05
# ----------------------------------------


class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node

		else:
			self.tail.next = node
			self.tail = node

	def is_zero(self):
		if self.head is None:
			return True
		return False

	def len(self):
		if self.head is None:
			return 'Empty'
		else:
			count = 0
			while self.head:
				self.head = self.head.next
				count += 1
			return count

	def iter(self):
		if not self.head:
			return

		cur = self.head
		yield cur.data
		while cur.next:
			cur = cur.next
			yield cur.data

	def insert(self, idx, value):
		cur = self.head
		cur_idx = 0
		while cur_idx < idx - 1:
			cur = cur.next
			if cur is None:
				raise Exception('List length less than index')
			cur_idx += 1
		node = Node(value)
		node.next = cur.next
		cur.next = node
		if node.next is None:
			self.tail = node

	def remove(self, idx):
		cur = self.head
		cur_idx = 0
		while cur_idx < idx - 1:
			cur = cur.next
			if cur is None:
				raise Exception('List length less than index')
			cur_idx += 1
		cur.next = cur.next.next
		if cur.next is None:
			self.tail = cur


if __name__ == '__main__':
	linked_list = LinkedList()
	for i in range(10):
		linked_list.append(i)

	print(linked_list.len())

	# print(linked_list.is_zero())
	# linked_list.insert(3, 30)
	# linked_list.remove(4)
	# for node in linked_list.iter():
	# 	print(node)
