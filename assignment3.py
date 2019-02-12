import time

def functionTimer(f, input):
	time1 = time.time()
	f(input)
	time2 = time.time()
	return time2 - time1

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

# testQueue = Queue()

# testQueue.enqueue(1)
# testQueue.enqueue(2)
# testQueue.enqueue(3)

# print(testQueue.dequeue())
# print(testQueue.dequeue())
# print(testQueue.dequeue())

# print(testQueue.isEmpty())

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

# testDeque = Deque()

# testDeque.addFront(1)
# testDeque.addRear(1)
# testDeque.removeFront()
# print(testDeque.size())