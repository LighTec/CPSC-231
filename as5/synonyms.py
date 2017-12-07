# function headers and the norm function are written by:
# Michael Guerzhoy. Last modified: Nov. 18, 2015.

# Implemented Methods and misc code written by:
# Kell Larson. Last modified: Dec. 7, 2017.

import re

# A vector is a dictionary of words, like this: ["man" : 1, "i" : 3] and so on.
def testSuite():
	sampleSentences = [["i", "am", "a", "sick", "man"], ["i", "am", "a", "spiteful", "man"], ["i", "am", "an", "unattractive", "man"], ["i", "believe", "my", "liver", "is", "diseased"],["however", "i", "know", "nothing", "at", "all", "about", "my","disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
	
	#print(build_semantic_descriptors(sampleSentences))

	words = [('man', 1, {'derp' : 1, 'a' : 2}), ('i' , 6, {'derp' : 3, 'b' : 1})]
	
	fileNames = ["Swanns Way"]#, "War and Peace"]
	print(build_semantic_descriptors_from_files(fileNames))
	#print(cosine_similarity(words[0][2], words[1][2]))
	
	# This needs to work
	#print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
	#sample_dict = {	"man" : {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1}, "liver" : {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}}
	#print(cosine_similarity(sample_dict["man"], sample_dict["liver"]))


def main():
	testSuite()

def norm(vec):
#Return the norm of a vector stored as a dictionary,
#as described in the handout for Project 3.
	sum_of_squares = 0.0  # floating point to handle large numbers
	for x in vec:
		sum_of_squares += vec[x] * vec[x]
	return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
	sqrtAmt1 = 0
	sqrtAmt2 = 0
	topNum = 0
	# init equation here
	for word1 in vec1:
		sqrtAmt1 += vec1[word1] ** 2
	# add it to the equation

	for word2 in vec2:
		sqrtAmt2 += vec2[word2] ** 2
	# add it to the equation
	for word1 in vec1:
		for word2 in vec2:
			if(word1 == word2):
				topNum = topNum + (vec1[word1] * vec2[word1])

	# do the sqrt here
	sqrtAmt = sqrtAmt1 * sqrtAmt2
	sqrtAmt = sqrtAmt ** (1/2)
	#print(sqrtAmt)
	return (topNum / sqrtAmt)

def build_semantic_descriptors(sentences):
	finalDict = {} # master list
	
	for currentSentence in sentences:
		for word in currentSentence:
			if word not in finalDict:
				finalDict.update({word : {}})
			for wordToAdd in currentSentence:
				if wordToAdd != word:
					if wordToAdd not in finalDict[word]:
						finalDict[word].update({wordToAdd : 1})
					else:
						finalDict[word][wordToAdd] = (finalDict[word][wordToAdd] + 1)
	return finalDict

def build_semantic_descriptors_from_files(filenames):
	# -*- coding: utf-8 -*-
	
	sentences = []

	for filename in filenames:
		f = open(filename, "r", encoding="utf-8")
		text = f.read()
		f.close()

		# Code from StackOverflow, tokenizing sentences without 
		# breaking apart sentences due to name prefixes or other things.
		# modified from source, removed the implemented 
		# Link: https://stackoverflow.com/questions/4576077/python-split-text-on-sentences

		# Pad the text with spaces at both ends
		text = " " + text + "  "
		# Remove the gutenberg website, causes parsing errors
		text = text.replace("http://www.gutenberg.org"," ")
		# Remove next line command
		text = text.replace("\n"," ")
		# if there 
		if "”" in text:
			text = text.replace(".”","”.")
		if "!" in text:
			text = text.replace("!\"","\"!")
		if "?" in text:
			text = text.replace("?\"","\"?")
		text = text.replace(".","<stop>")
		text = text.replace("?","<stop>")
		text = text.replace("!","<stop>")
		sentences = text.split("<stop>")
		sentences = sentences[:-1]
		sentences = [s.strip() for s in sentences]
		
		#END StackOverflow code

	tokenSentences = []
	for sentence in sentences:
		tokenSentences.append(sentence.split())
	builtDescriptors = build_semantic_descriptors(tokenSentences)
	return builtDescriptors
	

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
	print("Incomplete")

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
	print("Incomplete")

main()
