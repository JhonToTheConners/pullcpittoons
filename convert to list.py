#!"C:\Program Files (x86)\py\python.exe"
# -*- coding: utf-8 -*-

a_file = open("guildpage.txt", "r")
list_lists = []
for line in a_file:
    stripped_line = line.strip()
    list_lists.append(stripped_line)
a_file.close()

listofids = []
listofnames = []
print(list_lists)
for item in range(len(list_lists)):
    if list_lists[item - 1] == "<tr>":
        listofids.append(list_lists[item + 1])
        listofnames.append(list_lists[item])
del listofids[0]
del listofnames[0]
print(listofnames)
listofidscutdown = []
swgohpagelist = []
for id in listofids:
    listofidscutdown.append(id[9:22])
for cutdownid in listofidscutdown:
    indexed = listofidscutdown.index(cutdownid)
    newstringstring = listofnames[indexed].replace('"', '')
    newnewstring = ''.join(e for e in newstringstring if e.isalnum())
    swgohpagelist.append("curl https://swgoh.gg" + cutdownid + 'characters/ >> "pages/' + newnewstring[15:] + '.txt" \n')
print(swgohpagelist)
f_file = open("swgohpages.sh", "a")
for i in swgohpagelist:
    f_file.write(i)
