"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
t = turtle.Turtle()
t.color("HotPink")
for i in range(4):
    t.forward(90)
    t.left(90)
for i in range(2):
    t.left(45)
    t.forward(90)
for i in range(3):
    t.right(90)
    t.forward(90)
t.right(180)
t.forward(90)
t.right(135)
t.forward(90)
t.right(45)
t.forward(90)
t.right(90)
t.forward(90)
t.right(45)
t.forward(90)
t.right(45)
t.forward(90)
t.right(135)
t.forward(90)

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""

def DrawRectangle(Anyturtle, l , w):
    l = 60
    w = 100
    t = Anyturtle

t = turtle.Turtle
l = 70
w = 100
Anyturtle = t

DrawRectangle()
