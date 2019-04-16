
#to run: python3 hunpos_eval.py fi_hunpos_test fi_hunpos_out
import sys

test_file = open(sys.argv[1])
output_file = open(sys.argv[2])
identical_lines = 0
test_file_lines = []
for line in test_file: 
	test_file_lines.append(line)
i = 0
for line in output_file: 
	if line.strip() == test_file_lines[i].strip(): identical_lines += 1
	i += 1
print(100 * identical_lines/i)