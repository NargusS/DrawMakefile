import csv
import sys
from xml.etree import ElementPath

def	check_args_and_print(str, islast):
	if (str == "1"):
		print("$(NOIR)  $(RESET)", end="");
	elif (str == "2"):
		print("$(BLANC)  $(RESET)", end="");
	elif (str == "3"):
		print("$(BLEU)  $(RESET)", end="");
	elif (str == "4"):
		print("$(ROUGE)  $(RESET)", end="");
	elif (str == "5"):
		print("$(JAUNE)  $(RESET)", end="");
	elif (str == "6"):
		print("$(VERT)  $(RESET)", end="");
	elif (str == "7"):
		print("$(ROSE)  $(RESET)", end="");
	elif (str == "8"):
		print("$(CYAN)  $(RESET)", end="");
	else:
		print("  ", end="");
	if (islast):
		print("\\n\"");

def	read_csv(filename):
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|');
		i = 0;
		for row in csvfile:
			if (i == 26):
				return;
			print("@printf \"", end="");
			elems = row.split(",");
			for elem in elems:
				if (elem == elems[-1]):
					check_args_and_print(elem[:-2],True);
				else:
					check_args_and_print(elem,False);
			i+=1;


if __name__ == "__main__":
	read_csv(sys.argv[1]);