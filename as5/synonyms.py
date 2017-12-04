# function headers and the norm function are written by:
# Michael Guerzhoy. Last modified: Nov. 18, 2015.

# Code

import math

# A vector is a dictionary of words, like this: ["man" : 1, "i" : 3] and so on.

def main():
	words = [('man', 1, {'derp' : 1, 'a' : 2}), ('i' , 6, {'derp' : 3, 'b' : 1})]
	#print(cosine_similarity(words[0][2], words[1][2]))
	
	# This needs to work
	print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
	
	man = {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1}
	liver = {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}
	print(cosine_similarity(man,liver))

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
	print("Incomplete")

def build_semantic_descriptors_from_files(filenames):
	print("Incomplete")

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
	print("Incomplete")

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
	print("Incomplete")

main()
