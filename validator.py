#!/usr/bin/python
from Tkinter import *
from re import *
from tkMessageBox import *

root = Tk()
expression = ""

def messages(num):
	if num == 1:
		showinfo(message ="A Invalid Arithmatic Expression: Missing Arithmatic Operators/Operands")
	if num == 2:
		showinfo(message="A Invalid Arithmatic Expression: Mismatch Parentheses")
	if num == 3:
		showinfo(message="A Valid Arithmatic Expression")

def operands(expression):
	string = expression.replace(" ", "")
	string = string.replace("(","")
	string = string.replace(")","")
	print string
	chars = set('+-*/')
	stack = list()
	top = -1
	for c in string:
		if c.isdigit() == True:
			if top != -1:
				if stack[top].isalpha():
					return 1
			stack.append(c)
			top = top + 1
		elif c == '*' or c == '/' or c == '+' or c == '-':
			if top == -1:
				return 1
			if stack[top].isalpha():
				stack.pop()
				top = top - 1
			else:
				while stack[top].isdigit():
					stack.pop()
					top = top - 1
					if top == -1:
						break
		elif c.isalpha() == True:
			if top == -1:
				stack.append(c)
				top = top + 1
			else:
				return 1
	if len(stack) == 0:
		return 1
	else:
		return 3






def parentheses(expression):
	stack = list()
	num = 0
	for c in expression:
		if c == '(':
			stack.append(c)
		elif c == ')':
			if len(stack) == 0:
				return 2
			else:
				stack.pop()

	if len(stack) == 0:
		return 3
	else:
		return 2

def validate(expression):
	num = 0
	num = parentheses(expression)

	if(num != 2):
		num = operands(expression)

	messages(num)

def callback():
   expression = userInput.get()
   validate(expression)


def makeentry(parent, caption, width=None, **options):
   Label(parent, text=caption).pack(side=LEFT)
   entry = Entry(parent, **options)
   if width:
       entry.config(width=width)
   entry.pack(side=LEFT)
   return entry


userInput = makeentry(root, "Expression:", 60)

b = Button(root, text="Validate", width=10, command=callback)
b.pack()


mainloop()
