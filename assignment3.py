import time

def functionTimer(f, input):
	time1 = time.time()
	f(input)
	time2 = time.time()
	return time2 - time1

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
            itemNode = Node(item)
            if pos == 0:
                self.add(itemNode)
            currentSelection = self.head
            count = 0
            while count < self.size() - 1:
                self.index(currentSelection().getNextNode()) != pos:
                currentSelection = currentSelection.getNextNode()
            currentSelection.setNextNode(itemNode)

	# def pop(self):


	# def pop(self, pos):


	def print(self):
		print("[ ", end = '')
		node = self.head
		while(not node == None):
			print(str(node.getData())+" ", end = '')
			node = node.getNextNode()
		print("]")

def main():
	sampleNode1 = Node(3)
	sampleNode2 = Node(50)
	linked1 = Linked_List()
	linked1.add(1)
	linked1.add(2)
	linked1.add(10)
	linked1.print()
	linked1.insert(0,9)
	linked1.print()

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

if __name__ == '__main__':
	main()
