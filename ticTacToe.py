#!/usr/bin/python
from Tkinter import *
from re import *
from tkMessageBox import *

def changeText(root,text, turn, array, index):
	if text.get() != "":
		return
	if turn[0] % 2 == 0:
		text.set("x")
		turn.pop()
		turn.append(1)
		array[index] = "x"
	else:
		text.set("o")
		turn.pop()
		turn.append(0)
		array[index] = "o"
	checkWinner(root, array)

def checkWinner(root, array):
	#horizontal
	if array[0] == array[1] == array[2] and array[0] != "":
		showinfo(message = (array[0]+ " is winner"))
	elif array[3] == array[4] == array[5] and array[3] != "":
		showinfo(message = (array[3]+ " is winner"))
	elif array[6] == array[7] == array[8] and array[6] != "":
		showinfo(message = (array[6]+ " is winner"))
		#vertical
	elif array[0] == array[3] == array[6] and array[0] != "":
		showinfo(message = (array[0]+ " is winner"))
		root.destroy()
	elif array[2] == array[5] == array[7] and array[2] != "":
		showinfo(message = (array[2]+ " is winner"))
		root.destroy()
	elif array[3] == array[6] == array[8] and array[3] != "":
		showinfo(message = (array[3]+ " is winner"))
		root.destroy()
		#diagonal
	elif array[0] == array[4] == array[8] and array[0] != "":
		showinfo(message = (array[0] + " is winner"))
		root.destroy()
	elif array[2] == array[4] == array[6] and array[2] != "":
		showinfo(message = (array[2] + " is winner"))
		root.destroy()
	elif array[0] != "" and array[1] != "" and array[2] != "" and array[3] != "" and array[4] != "" and array[5] != "" and array[6] != "" and array[7] != "":
		if array[8] != "":
			showinfo(message = "Tie Game")
			root.destroy()

array = ["","","","","","","","",""]
turn = [0]
root = Tk()
frame = Frame(root, bg="#f2f2f2")
frame.pack()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()

B1 = Button(frame, text="", width=30, textvariable= text1, command = lambda: changeText(root, text1, turn, array, 0))
B2 = Button(frame, text="", width=30, textvariable= text2, command = lambda: changeText(root, text2, turn, array, 1))
B3 = Button(frame, text="", width=30, textvariable= text3, command = lambda: changeText(root, text3, turn, array, 2))

B4 = Button(frame, text="", width=30, textvariable= text4, command = lambda: changeText(root, text4, turn, array, 3))
B5 = Button(frame, text="", width=30, textvariable= text5, command = lambda: changeText(root, text5, turn, array, 4))
B6 = Button(frame, text="", width=30, textvariable= text6, command = lambda: changeText(root, text6, turn, array, 5))

B7 = Button(frame, text="", width=30, textvariable= text7, command = lambda: changeText(root, text7, turn, array, 6))
B8 = Button(frame, text="", width=30, textvariable= text8, command = lambda: changeText(root, text8, turn, array, 7))
B9 = Button(frame, text="", width=30, textvariable= text9, command = lambda: changeText(root, text9, turn, array, 8))

B1.grid(row = 0, column = 0, rowspan = 5)
B2.grid(row = 0, column = 1, rowspan = 5)
B3.grid(row = 0, column = 2, rowspan = 5)

B4.grid(row = 6, column = 0, rowspan = 5)
B5.grid(row = 6, column = 1, rowspan = 5)
B6.grid(row = 6, column = 2, rowspan = 5)

B7.grid(row = 11, column = 0, rowspan = 5)
B8.grid(row = 11, column = 1, rowspan = 5)
B9.grid(row = 11, column = 2, rowspan = 5)

mainloop()
