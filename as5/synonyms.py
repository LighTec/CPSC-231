# function headers and the norm function are written by:
# Michael Guerzhoy. Last modified: Nov. 18, 2015.

# Code

import math

# A vector is a dictionary of words, like this: ["man" : 1, "i" : 3] and so on.

def norm(vec):
    	'''Return the norm of a vector stored as a dictionary,
    	as described in the handout for Project 3.
    	'''
    
    	sum_of_squares = 0.0  # floating point to handle large numbers
    	for x in vec:
        	sum_of_squares += vec[x] * vec[x]

    	return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
	# init equation here
	for word1 in vec1:
		for word2 in vec2:
			if(word1 == word2):
				# add it to the equation
    	# do the sqrt here
	pass

def build_semantic_descriptors(sentences):
    	pass

def build_semantic_descriptors_from_files(filenames):
    	pass



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    	pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    	pass
