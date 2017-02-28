#!/usr/bin/python

userInput = 0
index = -1
first = ""
last = ""
num = 0
student = []
LIST = []

while userInput != 6:
	print "1.  Print all students"
	print "2.  Add a student to the list"
	print "3.  Print the information of next student"
	print "4.  Print the information of previous student"
	print "5.  Save  the  entire  list  of  students  in  a  file  named student.txt"
	print "6. Quit"

	userInput = input("Please choose an option: ")

	if (userInput == 1):
		print "First Name Last Name Student ID"
		for x in LIST:
			print x[0], "\t", x[1], "\t", x[2]
		print

	if (userInput == 2):
		first = raw_input("Enter First Name: ")
		last = raw_input("Enter Last Name: ")
		num = raw_input("Enter a Number: ")
		student = [first, last, num]
		LIST.append(student)

		index = index + 1

	if (userInput == 3):
		print "First Name Last Name Student ID"

		index = index + 1
		if (index == len(LIST)):
			index = 0;

		print LIST[index][0], "\t", LIST[index][1], "\t", LIST[index][2]
		print

	if (userInput == 4):
		print "First Name Last Name Student ID"

		index = index - 1
		if (index == -1):
			index = len(LIST) - 1;

		print LIST[index][0], "\t", LIST[index][1], "\t", LIST[index][2]
		print

	if (userInput == 5):
		stu = open("student.txt", "w", 0)
		stu.write("First Name Last Name Student ID\n")

		for x in LIST:
			stu.write(x[0] + "\t" + x[1] + "\t" + x[2] + "\n")

		stu.close()

n = nextButton(root, text=">", width=10, command=callback)
p = prevButton(root, text="<", width=10, command=callback)
l = lastButton(root, text=">>", width=10, command=callback)
f = firstButton(root, text="<<", width=10, command=callback)
b.pack()


mainloop()
