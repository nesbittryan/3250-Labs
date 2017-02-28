#!/usr/bin/python
from Tkinter import *
from re import *
from tkMessageBox import *

def AddToEntry(entry, value):
	entry.delete(0,END)
	entry.insert(0, value)

def makeentry(parent, caption, width=None, **options):
   Label(parent, text=caption).pack(side=LEFT)
   entry = Entry(parent, **options)
   if width:
       entry.config(width=width)
   entry.pack(side=LEFT)
   return entry

def loadFile(LIST, index,firstBox, lastBox, idBox):
	LIST = []

	fpt=open('student.txt', 'r')
	dataFile = fpt.read()
	LIST=dataFile.split('\n')

	for x in range(len(LIST) - 1):
		student.append(LIST[x].split('\t'))

	AddToEntry(firstBox, student[index[0]][0])
	AddToEntry(lastBox, student[index[0]][1])
	AddToEntry(idBox, student[index[0]][2])

def nButton(LIST, index, firstBox, lastBox, idBox):
	index[0] = index[0] + 1
	if (index[0] == len(LIST)):
		index[0] = 0

	AddToEntry(firstBox, student[index[0]][0])
	AddToEntry(lastBox, student[index[0]][1])
	AddToEntry(idBox, student[index[0]][2])

def pButton(LIST, index, firstBox, lastBox, idBox):
	index[0] = index[0] - 1
	if (index[0] == -1):
		index[0] = len(LIST) - 1

	AddToEntry(firstBox, student[index[0]][0])
	AddToEntry(lastBox, student[index[0]][1])
	AddToEntry(idBox, student[index[0]][2])

def lButton(LIST, index, firstBox, lastBox, idBox):
	index[0] = len(LIST) - 1

	AddToEntry(firstBox, student[index[0]][0])
	AddToEntry(lastBox, student[index[0]][1])
	AddToEntry(idBox, student[index[0]][2])

def fButton(LIST, index, firstBox, lastBox, idBox):
	index[0] = 0

	AddToEntry(firstBox, student[index[0]][0])
	AddToEntry(lastBox, student[index[0]][1])
	AddToEntry(idBox, student[index[0]][2])

userInput = 0
index = [0]
first = ""
last = ""
num = 0
student = []

root = Tk()

load = Button(root, text="Load:", width=10, command=lambda: loadFile(student, index, firstBox, lastBox, idBox))
n = Button(root, text=">", width=10, command=lambda: nButton(student, index, firstBox, lastBox, idBox))
p = Button(root, text="<", width=10, command=lambda: pButton(student, index, firstBox, lastBox, idBox))
l = Button(root, text=">>", width=10, command=lambda: lButton(student, index, firstBox, lastBox, idBox))
f = Button(root, text="<<", width=10, command=lambda: fButton(student, index, firstBox, lastBox, idBox))

firstBox =  makeentry(root, "First",20)
lastBox =  makeentry(root, "Last",20)
idBox =  makeentry(root, "ID",20)

load.pack()
n.pack()
p.pack()
l.pack()
f.pack()


mainloop()
