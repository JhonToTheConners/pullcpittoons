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
	arr = os.listdir("C:/Users/JB/Desktop/cpit script/pages/")
	print(arr)
	for file in arr:
		print(file)
		os.remove("C:/Users/JB/Desktop/cpit script/pages/" + file)
except:
	print("test3")
try:
	os.remove("guildroster.txt")
except:
	print("test3")
quit()