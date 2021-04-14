import os
try:
	os.remove("guildpage.txt")
except:
	print("test")
try:
	os.remove("swgohpages.sh")
except:
	print("test2")
try:
	arr = os.listdir(os.getcwd() + "/pages/")
	print(arr)
	for file in arr:
		print(file)
		os.remove(os.getcwd() + "/pages/" + file)
except:
	print("test3")
try:
	os.remove("guildroster.txt")
except:
	print("test3")
try:
	os.remove("guildteams.txt")
except:
	print("test4")
quit()