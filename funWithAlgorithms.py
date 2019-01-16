######################################################################
#                  Assignment 1: Fun With Algorithms                 #
#  Programmers: David Vandiver, Ashley Carlson, Fernando Espinoza    #
#  Course: CS301-009                                                 #
#  Date: 1/10/19                                                     #                                                                 #
######################################################################

#1.********************************************************************
def firstnsum(n):
	"""Sums the first n integers starting at 0"""
	return sum(range(n+1))

# print(firstnsum(100))

#2.********************************************************************
def checkValid(ex):
	"""Checks if a string ex is in words.txt"""
	fin = open('words.txt')
	for line in fin:
		word = line.strip() #remove newlines
		if word == ex.lower():
			return True
	return False

# print(checkValid("aa"))
# print(checkValid("weoigjrk"))
# print(checkValid("violet"))

#3.********************************************************************
def letterCount(w):
	"""Counts the number of characters in a word and maps into a dictionary"""
	di = {} #initiate dictionary
	for l in w:
		if l not in di: #creates key if not present
			di[l] = 1
		else:
			di[l] += 1 #add to value
	return di

# print(letterCount("football"))

def checkScramble(word1, word2, useAll=False, onlyTiles=False):
	"""Returns whether or not a word can be made from the given tiles.
	   Optional useAll and onlyTiles parameters allow for further
	   conditions in other functions."""
	w1 = letterCount(word1)
	w2 = letterCount(word2)
	if useAll: #if the word must use all of the tiles
		return w1 == w2
	else: #if the second word can be made from any number of the tiles
		for k,v in w2.items():
			if onlyTiles: #if the word must only use any num of tiles
				if k not in w1.keys():
					return False
			else:
				if k not in w1.keys() or w2[k] > w1[k]:
					return False
	return True

# print(checkScramble("football", "ball")) #True
# print(checkScramble("retinas", "nastier")) #True
# print(checkScramble("retina", "nastier")) #False

#4.********************************************************************
def findAll(tiles):
	"""Searches the words document for all possible scrambles
	   of the given tiles"""
	matches = [] #list containing all matched scrambles
	fin = open('words.txt')
	for line in fin:
		word = line.strip() #remove newlines
		if checkScramble(tiles, word, True): #uses useAll to use all tiles
			matches.append(word)
	return matches

# print(letterCount("retains"))
# print(letterCount("anestri"))
# print(findAll("retains")) #['anestri, 'nastier', 'ratines', 'retains',
                          # 'retinas', 'retsina', 'stainer', 'stearin']

#5.********************************************************************
def spellingBee(centerLetter, *args):
	"""Function for NYTimes Spelling Bee game. Takes in a center letter
	   as well as any number of outer letters. Looks for 5+ letter words
	   that use center at least once, with any repetition."""
	score = 0
	matches = []
	tiles = (''.join(args) + centerLetter).lower() #combine args
	fin = open('words.txt')
	for line in fin:
		word = line.strip() #remove newlines
		if len(word) >= 5 and centerLetter.lower() in word: #parameters
			if checkScramble(tiles, word, onlyTiles=True):
				matches.append(word)
				if checkScramble(word, tiles): 
					score += 3 #adds 3 pts if word uses all letters
				else:
					score += 1
	return matches, score

# print(spellingBee('L', 'A', 'B', 'C', 'I', 'N', 'R'))

#6.********************************************************************
def bingoFinder():
	"""Searches for all possible bingos in words.txt and finds the most
	   common combinations of letters"""
	comboCounter = [] #stores dictionaries in one large dictionary
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		counted = letterCount(word)
		if len(word) == 8 and word not in comboCounter: #at least 8 chars for bingo
			matches = findAll(word)
			print(matches)
			if len(matches) >= 2:
				for match in matches:
					comboCounter.append(match)
	return comboCounter

# def printonly8():
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		if len(word) == 8:
# 			print(word)

# printonly8()
bingoFinder()