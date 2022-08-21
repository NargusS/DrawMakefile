import csv
import sys
from xml.etree import ElementPath

def	choose_color(str):
	if (str == "1"):
		return("$(NOIR)  ")
	elif (str == "2"):
		return("$(BLANC)  ");
	elif (str == "3"):
		return("$(BLEU)  ");
	elif (str == "4"):
		return("$(ROUGE)  ");
	elif (str == "5"):
		return("$(JAUNE)  ");
	elif (str == "6"):
		return("$(VERT)  ");
	elif (str == "7"):
		return("$(ROSE)  ");
	elif (str == "8"):
		return("$(CYAN)  ");
	else:
		return ("  ");

def	do_line(elems):
	str = "@printf \"";
	last_color = "";
	for	elem in range(0, len(elems)):
		if(elem == len(elems) - 1):
			if (elems[elem][:-2] == last_color):
				str += "  $(RESET)";
			else:
				if (elem != 0):
					str += "$(RESET)";
				str += choose_color(elems[elem][:-2]);
				str += "$(RESET)";
			str += ("\\n\"");
		elif (elems[elem] == last_color):
			str += "  ";
		else:
			str += "$(RESET)";
			str += choose_color(elems[elem]);
		last_color = elems[elem];
	print(str);

			

def	read_csv(filename):
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|');
		i = 0;
		for row in csvfile:
			if (i == 26):
				return;
			elems = row.split(",");
			do_line(elems);
			i+=1;


if __name__ == "__main__":
	read_csv(sys.argv[1]);