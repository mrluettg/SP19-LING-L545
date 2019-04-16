import re
import sys
trainingFile = open(sys.argv[1])
outputFile = open("new_dictionary.txt", 'w')
for line in trainingFile: 
	if re.search('[0-9]', line[0]):
		lineList = line.split("\t")
		print(lineList[1])


