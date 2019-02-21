class Node:
	def __init__(self, data):
		self.node = data
		self.nextnode = None

	def getData(self):
		return self.node

	def setData(self, input_data):
		self.node = input_data

	def setNextNode(self, data):
		self.nextnode = data

	def getNextNode(self):
		return self.nextnode

class Linked_List:
	def __init__(self):
		self.head = None

	def add(self, item):
		newNode = Node(item)
		newNode.setNextNode(self.head)
		self.head = newNode

	def remove(self, item):
		if self.head.getData() == item:
			self.head = self.head.getNextNode()
			return
		currentSelection = self.head
		while currentSelection.getNextNode().getData() != item:
			currentSelection = currentSelection.nextnode
		currentSelection.setNextNode((currentSelection).getNextNode().getNextNode())

	def search(self, item):
		currentSelection = self.head
		while currentSelection.getData() != item:
			if currentSelection.getNextNode() == None:
				return False
			currentSelection = currentSelection.getNextNode()
		return True

	def isEmpty(self):
		return self.head == None
			
	def size(self):
		count = 0
		currentSelection = self.head
		while currentSelection != None:
			count += 1
			currentSelection = currentSelection.getNextNode()
		return count

	def append(self, item):
		currentSelection = self.head
		while currentSelection.getNextNode() != None:
			currentSelection = currentSelection.getNextNode()
		itemNode = Node(item)
		currentSelection.setNextNode(itemNode)

	def index(self, item):
		if not (self.search(item)):
			return False
		count = 0
		currentSelection = self.head
		while currentSelection.getData() != item:
			count += 1
			currentSelection = currentSelection.getNextNode()
		return count

	def insert(self, pos, item):
		if self.size() < pos:
			raise(IndexError)
		if pos == 0:
			self.add(item)
			return
		currentSelection = self.head
		count = 1
		while count < self.size()+1:
			if count == pos:
				itemNode = Node(item)
				itemNode.setNextNode(currentSelection.getNextNode())
				currentSelection.setNextNode(itemNode)
				return
			currentSelection = currentSelection.getNextNode()
			count += 1

	def pop(self):
		item = self.head
		while item.getNextNode() != None:
			item = item.getNextNode()
		self.remove(item.getData())
		return item

	def popPos(self, pos):
		if self.size() < pos:
			raise(IndexError)
		if pos == 0:
			item = self.head
			self.remove(self.head.getData())
			return self.head
		item = self.head
		count = 0
		while count < self.size()+1:
			if count == pos:
				self.remove(item.getData())
				return item
			item = item.getNextNode()
			count += 1

	def print(self):
		print("[ ", end = '')
		node = self.head
		while(not node == None):
			print(str(node.getData())+" ", end = '')
			node = node.getNextNode()
		print("]")

class DoubleNode:
	def __init__(self, data, previousn, nextn):
		self.node = data
		self.previousnode = previousn
		self.nextnode = nextn

	def getData(self):
		return self.node

	def setData(self, input_data):
		self.node = input_data

	def setNextNode(self, data):
		self.nextnode = data

	def getNextNode(self):
		return self.nextnode

	def setPreviousNode(self, data):
		self.previousnode = data

	def getPreviousNode(self):
		return self.previousnode

class Doubly_Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, item):
		self.head = DoubleNode(item, None, self.head)
		try:
			self.head.getNextNode().setPreviousNode(self.head)
		except:
			self.tail = self.head

	def remove(self, item):
		if self.head.getData() == item:
			self.head = self.head.getNextNode()
			return
		elif self.tail.getData() == item:
			self.tail = self.tail.getPreviousNode()
			self.tail.setNextNode(None)
			return
		currentSelection = self.head
		while currentSelection.getNextNode().getData() != item:
			currentSelection = currentSelection.getNextNode()
		currentSelection.setNextNode((currentSelection).getNextNode().getNextNode())
		currentSelection.getNextNode().setPreviousNode(currentSelection)

	def search(self, item):
		currentSelection = self.head
		while currentSelection.getData() != item:
			if currentSelection.getNextNode() == None:
				return False
			currentSelection = currentSelection.getNextNode()
		return True

	def isEmpty(self):
		return self.head == None
			
	def size(self):
		count = 0
		currentSelection = self.head
		while currentSelection != None:
			count += 1
			currentSelection = currentSelection.getNextNode()
		return count

	def append(self, item):
		oldTail = self.tail
		self.tail = DoubleNode(item, oldTail, None)

	def index(self, item):
		if not (self.search(item)):
			return False
		count = 0
		currentSelection = self.head
		while currentSelection.getData() != item:
			count += 1
			currentSelection = currentSelection.getNextNode()
		return count

	def insert(self, pos, item):
		if self.size() < pos:
			raise(IndexError)
		if pos == 0:
			self.add(item)
			return
		currentSelection = self.head
		count = 1
		while count < self.size()+1:
			if count == pos:
				itemNode = DoubleNode(item, currentSelection, currentSelection.getNextNode())
				currentSelection.setNextNode(itemNode)
				itemNode.getNextNode().setPreviousNode(itemNode)
				return
			currentSelection = currentSelection.getNextNode()
			count += 1

	def pop(self):
		item = self.tail
		self.tail = self.tail.getPreviousNode()
		self.tail.setNextNode(None)
		return item

	def popPos(self, pos):
		if self.size() < pos:
			raise(IndexError)
		if pos == 0:
			item = self.head
			self.remove(self.head.getData())
			return item
		elif pos == self.size():
			return self.pop()
		item = self.head
		count = 0
		while count < self.size()+1:
			if count == pos:
				self.remove(item.getData())
				return item
			item = item.getNextNode()
			count += 1

	def print(self):
		print("[ ", end = '')
		node = self.head
		while(not node == None):
			print(str(node.getData())+" ", end = '')
			node = node.getNextNode()
		print("]")

class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		return (len(self.stack) == 0)

	def size(self):
		return len(self.stack)

class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.insert(0,item)

	def dequeue(self):
		return self.queue.pop(0)

	def isEmpty(self):
		return (len(self.queue) == 0)

	def size(self):
		return len(self.queue)

class Deque:
	def __init__(self):
		self.deque = []

	def addFront(self, item):
		self.deque.insert(0,item)

	def addRear(self, item):
		self.deque.append(item)

	def removeFront(self):
		return self.deque.pop(0)

	def removeRear(self):
		return self.deque.pop()

	def isEmpty(self):
		return len(self.deque) == 0

	def size(self):
		return len(self.deque)

def rpn_eval(input_string):
	input_list = input_string.split(' ')
	rpn_stack = Stack()
	for item in input_list:
		if item == "+":
			n1 = rpn_stack.pop()
			n2 = rpn_stack.pop()
			rpn_stack.push(str(int(n1)+int(n2)))

def main():
	#-------------Linked_List methods -------------#
	# linked1 = Linked_List()
	# linked1.add(1)
	# linked1.add(2)
	# linked1.add(10)
	# linked1.print()
	# linked1.add(12)
	# linked1.print()
	# linked1.remove(12)
	# linked1.print()
	# print(linked1.search(2))
	# print(linked1.search(20))
	# print(linked1.isEmpty())
	# print(linked1.size())
	# linked1.append(12)
	# linked1.print()
	# print(linked1.index(2))
	# linked1.insert(2,5)
	# linked1.print()
	# print(linked1.pop())
	# print(linked1.popPos(0))
	# linked1.print()
	#----------Doubly_Linked_List methods----------#
	# linked2 = Linked_List()
	# linked2.add(1)
	# linked2.add(2)
	# linked2.add(10)
	# linked2.print()
	# linked2.add(12)
	# linked2.print()
	# linked2.remove(12)
	# linked2.print()
	# print(linked2.search(2))
	# print(linked2.search(20))
	# print(linked2.isEmpty())
	# print(linked2.size())
	# linked2.append(12)
	# linked2.print()
	# print(linked2.index(2))
	# linked2.insert(2,5)
	# linked2.print()
	# print(linked2.pop())
	# print(linked2.popPos(0))
	# linked2.print()

	# I think Python's internal list may be a doubly-linked list,
	# as it is able to do methods like appending much more quickly
	# than a regular linked-list would, and everything seems to
	# be much more efficiently done.

	#--------------Stack methods--------------#
	# testStack = Stack()
	# testStack.push(1)
	# testStack.push(2)
	# testStack.push(3)
	# print(testStack.peek())
	# print(testStack.pop())
	# print(testStack.size())
	# print(testStack.pop())
	# print(testStack.pop())
	# print(testStack.isEmpty())

	# All of the Stack methods make use of Python's built-in list
	# methods, so they will essentially the same running time.

	#--------------Queue methods-------------#
	# testQueue = Queue()
	# testQueue.enqueue(1)
	# testQueue.enqueue(2)
	# testQueue.enqueue(3)
	# print(testQueue.dequeue())
	# print(testQueue.dequeue())
	# print(testQueue.dequeue())
	# print(testQueue.isEmpty())

	# All Queue methods, like the Stack methods, use Python's built-in
	# list methods, and will have the same running time.

	#------------Deque methods---------------#
	# testDeque = Deque()
	# testDeque.addFront(1)
	# testDeque.addRear(1)
	# testDeque.removeFront()
	# print(testDeque.size())

	# Deque methods also use Python's built-in list methods, and will
	# have the same running time.

	#---------Reverse Polish Notation--------#

if __name__ == '__main__':
	main()
