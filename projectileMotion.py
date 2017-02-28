#!/usr/bin/python
import math
import Tkinter

#
#   frange
#   Floating point ranges!!!!
#
def frange(start, stop, inc):
    i = start
    while i < stop:
        yield i
        i += inc

#
#   toRadian
#   Convert degrees to radians.
#
def toRadian(degree):
    return float(degree) * (math.pi / 180.0)

#
#   flightTime
#   Calculate the total time the projectile is in the air.
#
def flightTime (velocityInitial, angle):
    return ((2 * velocityInitial) * math.sin(angle)) / 9.8

#
#   horizontalDistance
#   Calculate the projectile's horizontal distance x (from the launch position).
#
def horizontalDistance(velocityInitial, angle, time):
    return velocityInitial * time * math.cos(angle)

#
#   verticalDistance
#   Calculate vertical distance h (from the ground) at time t.
#
def verticalDistance(velocityInitial,angle, time):
    return (-1/2 * 9.8 * time * time) + (velocityInitial * time * math.sin(angle))

#   Start Main Logic  #

#   Get angle, and initial velocity
angle = toRadian(78)
velocity = 102          #   Should probably get these from the GUI


#   Get total flight time
time = flightTime(velocity, angle)

l = []
count = 0
#   The list will l contain tuples of (x,y) points on the time interval of 0.1 seconds
for i in frange(0, time, 0.1):
    #   Create the point (x,y)
    tup1 = (horizontalDistance(velocity,angle,i),verticalDistance(velocity,angle,i))
    #   Display it
    print i,
    print " ",
    print tup1
    #   Add it to the list
    l.insert(count,tup1)
    count += 1

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, bg="white", height=650, width=1500)
canvas.pack()
xP = 0
yP = 649
for i in frange(0, time, 0.1):
    #   Create the point (x,y)
    x = horizontalDistance(velocity,angle,i)
    y = verticalDistance(velocity,angle,i)
    count += 1
    point = canvas.create_oval(x * 2 , -y * 2 + 649, x * 2, -y * 2 + 649, fill="black")
    lineV1 = canvas.create_line(x * 2,-y * 2 + 649,xP,yP, fill="red")
    xP = x * 2
    yP = -y * 2 + 649
    print (x * 2)
    print (-y * 2 + 749)

canvas.pack()
root.mainloop()
