import re
import sys
trainingFile = open(sys.argv[1])
outputFile = open("new_dictionary.txt", 'w')
sentence = ""
for line in trainingFile: 
	if re.search('[0-9]', line[0]):
		lineList = line.split("\t")
		sentence += lineList[1] + " "
	if re.search('# text = ', line): 
		print(sentence)
		sentence = ""
trainingFile.close()
outputFile.close()
		