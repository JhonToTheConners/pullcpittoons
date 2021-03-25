#!"C:\Program Files (x86)\py\python.exe"
# -*- coding: utf-8 -*-
import os
def shortenstring(string):
    shortstringpart1 = string[6:]
    shortstringpart2 = shortstringpart1[:-1]
    return shortstringpart2

newdict = {}
def findallr5(inputfile):
    templist = []
    ndlist = []
    stroffile = (os.getcwd() + "/pages/" + file)
    x_file = open(stroffile, "r")
    for line in x_file:
        stripped_line = line.strip()
        templist.append(stripped_line)
    for item in range(len(templist)):
        if templist[item - 1] == r'<div class="char-portrait-full-relic">5</div>' or templist[item - 1] == r'<div class="char-portrait-full-relic">6</div>' or templist[item - 1] == r'<div class="char-portrait-full-relic">7</div>':
            newvar = (templist[item - 11]).split()
            for newitem in newvar:
                if newitem.startswith("alt"):
                    for i in range(5):
                        try:
                            if newvar[newvar.index(newitem) + i].startswith("height"):
                                newstring = ""
                                for x in range(i):
                                    var = newvar.index(newitem)
                                    newstring = newstring + " " + newvar[var + x]             
                                ndlist.append(newstring)
                        except:
                            None
    global newdict
    newdict[inputfile] = ndlist
    



arr = os.listdir(os.getcwd() + "/pages/")
for file in arr:
    findallr5(file)
y_file = open("guildroster.txt", "a")
for item in newdict:
    y_file.write("\n \n" + item + "\n")
    listcounter = 0
    for listitem in newdict[item]:
        if listcounter == 7:
            listcounter = 0
            y_file.write("\n")
        listitemnum2 = shortenstring(listitem)
        y_file.write(listitemnum2 + "     ")
