import random
def generate(targetSentence, tagged):
	"""Generates a random sentence equal in format to a target"""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	randomSentence = ""
	for i in range(len(targetSentence)):
		if targetSentence[i] == " ": #if there's a space, keep it
			randomSentence += " "
		elif i in tagged: #if letter already matched, remain that letter
			randomSentence += targetSentence[i]
		else: #generate random letter otherwise
			randomSentence += alphabet[random.randint(0,25)]
	return randomSentence

def score(s1, s2):
	"""Compares target sentence to generated sentence and tags correct letters"""
	tagged = []
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			tagged.append(i) #if letters match, tag for keeping
	return tagged

def comparisonLoop(targetSentence):
	"""Continuously generates sentences to compare to the target
	   until the target is equal to the random sentence."""
	sentences = {} #stores all generated sentences
	tagged = []    #keeps track of values that won't change
	tries = 0      #number of tries at generation
	highScore = 0  #highest num of letters matched
	while True:
		ran = generate(targetSentence, tagged)
		tagged = score(ran, targetSentence)
		ranScore = len(tagged)
		if ranScore > highScore:
			highScore = ranScore
		sentences[ranScore] = ran
		if ranScore == len(targetSentence):
			print("Matched at" , tries , "tries!")
			break
		else:
			tries += 1
			if tries % 10 == 0:
				print("Highest score is" , highScore , "by" , sentences[highScore])

comparisonLoop("methinks it is like a weasel")
