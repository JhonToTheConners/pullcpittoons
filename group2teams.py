#!"C:\Program Files (x86)\py\python.exe"
# -*- coding: utf-8 -*-

def are_you_at_txt(matrix: List[str], line: int) -> bool:
	if ".txt" in matrix[line]:
		return True
	else:
		return False
def teamgenerator(matrix: List[str], line: int) -> None:
	pa = False
	gk = False
	jka = False
	at = False
	possiblepsubs = ['C-3PO', 'Grand Master Yoda']
	for i in range(500):
		if are_you_at_txt(matrix, line + i):
			nextplayerindex = i
			break
	for x in range(nextplayerindex+1):
		if "Padmé Amidala" in matrix[line+x] or "PadmÃ© Amidala" in matrix[line+x]:
			pa = True
		if "General Kenobi" in matrix[line+x]:
			gk = True

y_file = open("guildroster.txt", "r")
matrix = []
for line in y_file:
	matrix.append(line)
for item in matrix:
	if item == "\n":
		matrix.remove(item)
print(matrix)

for index in range(len(matrix)):
	if are_you_at_txt(matrix, index):
		teamgenerator(matrix, index)
	else:
		pass

