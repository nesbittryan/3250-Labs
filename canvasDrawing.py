#!/usr/bin/python
import Tkinter
import tkMessageBox

def divideCanvas():
    lineV1 = canvas.create_line(99,0,99,399, fill="red")
    lineV2 = canvas.create_line(199,0,199,399, fill="red")
    lineV3 = canvas.create_line(299,0,299,399, fill="red")
    lineH1 = canvas.create_line(0,99,399,99, fill="red")
    lineH2 = canvas.create_line(0,199,399,199, fill="red")
    lineH3 = canvas.create_line(0,299,399,299, fill="red")

def drawCircle():
    circle = canvas.create_oval(99,99,299,299, fill="yellow")

root = Tkinter.Tk()

canvas = Tkinter.Canvas(root, bg="white", height=400, width=400)
B1 = Tkinter.Button(root, text ="Divide Canvas Area", command = divideCanvas)
B2 = Tkinter.Button(root, text ="Draw Circle", command = drawCircle)

canvas.pack()
B1.pack()
B2.pack()
root.mainloop()
