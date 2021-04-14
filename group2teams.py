#!"C:\Program Files (x86)\py\python.exe"
# -*- coding: utf-8 -*-
def are_you_at_txt(matrix, line: int) -> bool:
	if ".txt" in matrix[line]:
		return True
	else:
		return False
def del_item_from_str(str: str, item: str) -> str:
	itemindex = str.index(item)
	itemlength = len(item)
	newstring = str[0:itemindex] + str[itemindex+itemlength:]
	return newstring

def teamgenerator(matrix, line: int) -> None:
	currentstr = matrix[line + 1]
	player = matrix[line]
	padme = False
	GK = False
	JKA = False
	AT = False
	Shaak = False
	FIVES = False
	Rex = False
	ECHO = False
	ARC = False
	padmestring = ""
	shaaktroopersstring = ""
	if "PadmÃ© Amidala" in currentstr:
		padme = True
		currentstr = del_item_from_str(currentstr, "PadmÃ© Amidala")
	if "Padmé Amidala" in currentstr:
		padme = True
		currentstr = del_item_from_str(currentstr, "Padmé Amidala")
	if "General Kenobi" in currentstr:
		GK = True
		currentstr = del_item_from_str(currentstr, "General Kenobi")
	if "Jedi Knight Anakin" in currentstr:
		JKA = True
		currentstr = del_item_from_str(currentstr, "Jedi Knight Anakin")
	if "Ahsoka Tano" in currentstr:
		AT = True
		currentstr = del_item_from_str(currentstr, "Ahsoka Tano")
	if "Shaak Ti" in currentstr:
		Shaak = True
		currentstr = del_item_from_str(currentstr, "Shaak Ti")
	if "CT-5555 &quot;Fives&quot;" in currentstr:
		FIVES = True
		currentstr = del_item_from_str(currentstr, "CT-5555 &quot;Fives&quot;")
	if "CT-7567 &quot;Rex&quot;" in currentstr:
		Rex = True
		currentstr = del_item_from_str(currentstr, "CT-7567 &quot;Rex&quot;")
	if "CT-21-0408 &quot;Echo&quot;" in currentstr:
		ECHO = True
		currentstr = del_item_from_str(currentstr, "CT-21-0408 &quot;Echo&quot;")
	if "ARC Trooper" in currentstr:
		ARC = True
		currentstr = del_item_from_str(currentstr, "ARC Trooper")
	if padme and GK and JKA and AT:
		padmestring = "PADME"
	if Shaak and ECHO and FIVES and Rex and ARC:
		shaaktroopersstring = "SHAAKTROOPERS"
	new_file.write(player + "    " + padmestring + "  " + shaaktroopersstring + "     " + currentstr + "\n \n \n")
	
	

y_file = open("guildroster.txt", "r")
matrix = []
for line in y_file:
	matrix.append(line)
for item in matrix:
	if item == "\n":
		matrix.remove(item)
print(matrix)
new_file = open('guildteams.txt', 'a')
for index in range(len(matrix)):
	if are_you_at_txt(matrix, index):
		teamgenerator(matrix, index)
	else:
		pass
new_file.close
