#############################################
# David Vandiver                            #
# CS 301-009                                #
# Assignment 4 -- Searching lists           #
#############################################
def search_sorted_list(sorted_list, item, index=-1):
	"""
	Uses binary search to locate an item in a sorted list in
	O(logn) time.
	"""
	largest = sorted_list[-1]
	smallest = sorted_list[0]
	if index == -1:
		index = len(sorted_list) // 2
	if sorted_list[index] == item:
			return True
	else:
		if sorted_list[index] == largest or sorted_list[index] == smallest:
			return False
		if sorted_list[index] > item:
			return search_sorted_list(sorted_list, item, index // 2)
		else:
			return search_sorted_list(sorted_list, item, (index * 3) // 2)

class HashList:
	def __init__(self, length):
		self.data = []
		self.length = length
		for i in range(length):
			self.data.append('-') #placeholder character for empty slot

	def hashFunction(self, item):
		"""
		Finds an index for an item to be assigned using the remainder of the
		value divided by the number of indices.
		"""
		index = item % self.length 
		return index

	def put(self, item):
		"""
		Attempts to assign to hashFunction result by default, then increments
		up one index if the spot is already taken, until it finds one that
		isn't.
		"""
		index = self.hashFunction(item)
		count = 1
		while self.data[index] != '-':
			if count-1 == self.length:
				raise Exception("HashList is full!")
			if index != self.length-1:
				index += 1
			else:
				index = 0
			count += 1
		self.data[index] = item

	def contains(self, item):
		expected = item % self.length
		count = 1
		while self.data[expected] != item:
			if count == self.length:
				return False
			if expected != self.length-1:
				expected += 1
			else:
				expected = 0
			count += 1
		return True

	def items(self):
		itemlist = []
		for i in self.data:
			if i != '-':
				itemlist.append(i)
		return itemlist

def sort_list(ulist, newlist=[]):
	smallest = min(ulist)
	ulist.remove(smallest)
	newlist.append(smallest)
	if len(ulist) == 0:
		return newlist
	else:
		return sort_list(ulist, newlist)

def main():
	# print(search_sorted_list([1, 2, 3, 4, 5, 6, 7], 2))
	# print(search_sorted_list([1, 2, 3, 4, 5, 6, 7], 5))
	# print(search_sorted_list([1, 2, 3, 4, 5, 6, 7], 15))
	# print(search_sorted_list([1, 2, 3, 4, 5, 6, 7], 4))
	# print(search_sorted_list([1, 2, 3, 4, 5, 6, 7], 7))

	# hash = HashList(12)
	# # print(hash.hashFunction(16))
	# hash.put(12)
	# hash.put(8)
	# hash.put(2)
	# hash.put(56)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# # hash.put(12)
	# # hash.put(12)
	# # hash.put(12)
	# # hash.put(25)
	# print(hash.items())
	# print(hash.contains(12))
	# print(hash.contains(13))
	# print(hash.contains(2))

	# list1 = [5, 4, 10, 2, 12]
	# print(sort_list(list1))

# Defining the HashList runs in O(n) time, as it creates a list by defining
# n characters in that list. There isn't really a best or worst case scenario
# for this, it will always be O(n), where n is the size of the Hash list.
# The hashFunction() method runs in O(1) time,  running a simple operation.
# put() runs in linear O(n) time, as it relies on hashFunction()'s constant time
# to determine an index. It then executes operations using a loop, checking the
# entire list at worst. It will be O(1) at best and O(n) at worst.
# contains() is the same case as put(), as they both have very similar
# algorithms, with contains() checking for an a specified character instead
# of one any empty one. (O(1) at best, O(n) at worst).
# items() runs in linear time O(n), iterating through each item no matter what
# and appending it to a list if it is not a blank character.

# In order to turn this HashList into a dictionary, there would have to be
# functionality for assigning indices to values being added to the hash,
# instead of using a default modulo function that analyzes the data being added.
# In this way, the hash wouldn't have to pre-generate a list with a certain size,
# and would instead allow more flexibility with the order of things. This seems
# similar to the difference between a list and a linked list, in which the values
# are related to each other.

if __name__ == '__main__':
	main()