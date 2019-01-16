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

# print(firstnsum(100)) #5050

#2.********************************************************************
def checkValid(ex):
	"""Checks if a string ex is in words.txt"""
	fin = open('words.txt')
	for line in fin:
		word = line.strip() #remove newlines
		if word == ex.lower():
			return True
	return False

# print(checkValid("aa")) #True
# print(checkValid("weoigjrk")) #False
# print(checkValid("violet")) #True

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

# print(letterCount("football")) #{'f': 1, 'o': 2, 't': 1, 'b': 1a': 1, 'l': 2}

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
# print(checkScramble("nastier", "retina", True)) #False
# print(checkScramble("raaaaannnnn", "ran", onlyTiles=True)) #True

#4.********************************************************************
def findAll(tiles, words='words.txt'):
	"""Searches the words document for all possible scrambles
	   of the given tiles"""
	matches = [] #list containing all matched scrambles
	if words == 'words.txt':
		words = open('words.txt')
	for line in words:
		word = line.strip() #remove newlines
		if checkScramble(tiles, word, True): #uses useAll to use all tiles
			matches.append(word)
	return matches

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
# def bingoFinderOld():
# 	"""Searches for all possible bingos in words.txt and finds the most
# 	   common combinations of letters. This algorithm takes about
#      10 minutes to run."""
# 	eightLetters = []
# 	fin = open('words.txt')
# 	for line in fin:
# 		word = line.strip()
# 		if len(word) == 8: #must be 8 chars for bingo
# 			eightLetters.append(word)
# 	currentHigh = 0 #highest number of matched scrambles
# 	highestScoring = []
# 	for w in eightLetters:
# 		matches = findAll(w, eightLetters) #searches for all scrambled words
# 		# print(matches)
# 		if len(matches) >= currentHigh: #only shows record-holders
# 			print(matches)
# 			currentHigh = len(matches)
# 		for match in matches:
# 			eightLetters.remove(match) #removes ones already found

def bingoFinder():
	"""Counts the letters in every single 8-letter word (bingo) in words.txt
	   and stores them in a dictionary to show frequency. The letter
	   combo with the highest frequency value forms the most possible
	   bingos."""
	combinations = {} #stores all tile combinations
	eightLetters = [] #stores all words with 8 letters
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if len(word) == 8:
			eightLetters.append(word)
	for w in eightLetters:
		letters = [] #starts as a list for sorting
		wfreq = letterCount(w)
		sortItems = sorted(wfreq.items())
		for k,v in sortItems:
			for i in range(v): #makes sure repeat letters are included
				letters.append(k) 
		letters = tuple(letters) #converted to hashable type
		if letters not in combinations: 
			combinations[letters] = 1
		else:
			combinations[letters] += 1 #adds to frequency in combos
	currentHigh = 0
	highScorer = []
	for k,v in combinations.items():
		if v >= currentHigh: #only print and save if at least better than record
			print(k, v, "times.")
			highScorer = k
			currentHigh = v
	print("The most possible bingos is",currentHigh,"with",highScorer)


bingoFinder() #this algorithm is instantaneous
# bingoFinderAlt() #WARNING this algorithm takes a LONG time