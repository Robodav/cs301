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

testStack = Stack()

testStack.push(1)
testStack.push(2)
testStack.push(3)

print(testStack.peek())
print(testStack.pop())
print(testStack.size())
print(testStack.pop())
print(testStack.pop())
print(testStack.isEmpty())