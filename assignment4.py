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
		Finds an index for an item to be assigned, attempting to assign to the
		remainder of the item divided by the number of indices by default,
		then incrementing up one index if the spot is already taken.
		"""
		index = item % self.length 
		count = 0
		while self.data[index] != '-':
			if count == self.length:
				return -1 #tells put() function to raise exception when full
			if index != self.length-1:
				index += 1
			else:
				index = 0
			count += 1
		return index

	def put(self, item):
		index = self.hashFunction(item)
		if index != -1:
			self.data[self.hashFunction(item)] = item
		else:
			raise Exception("HashList is full!")

	def contains(self, item):
		expected = item % self.length
		count = 0
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

	# hash = HashList(13)
	# print(hash.hashFunction(16))
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
	# hash.put(12)
	# hash.put(12)
	# hash.put(12)
	# hash.put(25)
	# print(hash.items())
	# print(hash.contains(12))
	# print(hash.contains(13))
	# print(hash.contains(2))

	list1 = [5, 4, 10, 2, 12]
	print(sort_list(list1))

# Defining the HashList runs in O(n) time, as it creates a list by defining
# n characters in that list. There isn't really a best or worst case scenario
# for this, it will always be O(n), where n is the size of the Hash list.
# The hashFunction() method also runs in O(n) time, evaluating an index in
# constant time, then running through indices. Of course, it runs in O(n)
# only in the worst case, in which it would have to run through every index
# with max collisions. Otherwise, it would run in consant O(1) time.
# put() runs in the same time as hashFunction(), as it relies on hashFunction()
# to determine an index. It then executes operations in constant time, so
# it will be O(1) at best and O(n) at worst.
# contains() is the same case as hashFunction(), as they both have very similar
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