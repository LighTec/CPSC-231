# get input from test.txt, output with a print function
# Only lines with the substring "snake" get printed.

# By Kell Larson, timestamp 2 Nov, 14:56PM. 2017

def getInput():
	inputFile = open("test.txt", "r")
	txt = []
	while True:
		readLine = inputFile.readline()
		if(readLine == ""):
			break;
		txt.append(readLine)
	return txt

def main():
	s = getInput()
	printSnakes(s)

def printSnakes(s):
	for i in range(len(s)):
		if('snake' in s[i]):
			print(s[i])

main()
