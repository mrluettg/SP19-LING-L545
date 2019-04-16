import sys
import re

sentenceLst = []
for line in sys.stdin: 
	sentenceLst.append(line)

dictionaryFile = open(sys.argv[1])
dictList = []
for line in dictionaryFile: 
	line = line.strip("\n")
	dictList.append(line)

def tokenize(str): 
	if str:
		longestWord = ""
		i = 0
		currentWord = ""
		while i < len(str): 
			currentWord += str[i]
			if currentWord in dictList: 
				longestWord = currentWord
			i += 1
		return longestWord + " " +  tokenize(str[len(longestWord): ])
	else: return ""

for line in sentenceLst: 
	print("Sentence: " + line)
	line = line.strip("\n")
	line = tokenize(line)
	print("Tokenize: " + line)

