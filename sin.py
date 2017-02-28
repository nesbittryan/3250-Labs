#!/usr/bin/python
from __future__ import division 
from Tkinter import *
from re import *
from tkMessageBox import *
import math       

root = Tk()

def sinEquation(x,e):
	c = math.sin(x)
	n = 1
	y = 0
	while not condition(c, y, e):
		y = 0
		k = 0
		for i in range(n):
			y += term(x, k)
			k += 1
		n += 1
	cStr = "%.2f" % c
	yStr = "%.2f" % y
	nStr = str(n)
	diffStr = "%.2f" % abs(c-y)
	
	return "c = "+cStr+" y = "+yStr+" n = "+nStr+" |c-y| = "+diffStr

def toRadians(degrees):
	radians = float(degrees) * math.pi / 180.00
	return radians

def term(x, k):
    result = math.pow(-1, k) * (math.pow(x, 2*k +1)) / (math.factorial(2*k +1))
    return result

def condition(c, y, delta):
    value = math.fabs(c-y)
    return value < delta

def pressButton():
	e = float(eInput.get())
  	x = float(xInput.get())
	x = toRadians(x)
	myText = sinEquation(x,e)
	label_text.set(myText)
	return

def makeentry(parent, caption, width=None, **options):
   Label(parent, text=caption).pack(side=LEFT)
   entry = Entry(parent, **options)
   if width:
       entry.config(width=width)
   entry.pack(side=LEFT)
   return entry

#######################################################

eInput = makeentry(root, "Enter e" ,width=10)
xInput = makeentry(root, "Entry x" ,width=10)

label_text=StringVar()
labelTest= Label(root, textvariable=label_text,width=30)
labelTest.pack()

label1= "c = ___ y = ___ n = ___ |c-y| = ___"
label_text.set(label1)

bPress = Button(root, text="Begin Calculation", command=pressButton)
bPress.pack()

mainloop()