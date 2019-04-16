import sys

file = open(sys.argv[1])
for line in file:
	if line.strip(" ") == "\n" or line.strip(" ") == "": print("\n")
	elif line[0] == "#": continue
	else: 
		line_lst = line.split("\t")
		print(line_lst[1] + "\t" + line_lst[3])