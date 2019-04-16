import sys
import re
import matplotlib.pyplot as plt
#returns a tuple of the vo and ov (vo, ov) found in sentence.
#returns [1, 0] for vo, [0, 1] for ov 
def analyze_object(object_line): 
	line_lst = re.split(r'\t+', object_line)
	if line_lst[7] == "obj": 
		obj_num = line_lst[0]
		verb_num = line_lst[6]
		if int(obj_num) > int(verb_num): return (1, 0)
		else: return (0, 1)
def get_vo_ov_ratio(file_str): 
	langFile = open(file_str, 'r')
	sentence = ""
	total_ratio = [0, 0]
	for line in langFile:
		if line[0] == "#": continue
		if line.strip("/t") == "\n" or line.strip("/t") == "":continue
		else:
			line_lst = line.split()
			if line_lst[7] == "obj": 
				new_ratio = analyze_object(line)
				total_ratio[0] += new_ratio[0]
				total_ratio[1] += new_ratio[1]
			sentence += line
	total = total_ratio[0] + total_ratio[1]
	return (total_ratio[0]/total, total_ratio[1]/total)



#the languages used
files = ("br_keb-ud-test.conllu", 	#Breton
"cs_fictree-ud-train.conllu", 		#Czech
"en_pud-ud-test.conllu", 		#English
"es_gsd-ud-train.conllu", 		#Spanish
"eu_bdt-ud-train.conllu", 		#Basque
"fi_ftb-ud-train.conllu", 		#Finnish
"hy_armtdp-ud-train.conllu",		#Armenian
"ja_modern-ud-test.conllu", 		#Japanese
"th_pud-ud-test.conllu", 		#Thai
"tl_trg-ud-test.conllu", 		#Telugu
"vi_vtb-ud-train.conllu",		#Vietnamese
"yo_ytb-ud-test.conllu")		#Yoruba

#finds the language code and uses it as the label. 
def get_label(str): 
	label = ""
	for char in str: 
		if char == "_": return label
		else: label += char
def vo_ov_graph(): 
	labels = {}
	x = []#proportion of ov/vo_ov[1]
	y = []#proportion of vo/vo_ov[0]
	i = 0
	while i < len(files): 
		labels[i] = get_label(files[i])
		vo_ov = get_vo_ov_ratio(files[i])
		x.append(vo_ov[1])
		y.append(vo_ov[0])
		i += 1
	plt.plot(x, y, 'ro')
	plt.title('Relative word order of verb and object')
	plt.xlim([0,1]) # Set the x and y axis ranges
	plt.ylim([0,1])
	plt.xlabel('OV') # Set the x and y axis labels
	plt.ylabel('VO')
	for i in labels:  # Add labels to each of the points
    		plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
	plt.savefig(sys.argv[1])
	plt.show()
vo_ov_graph()
