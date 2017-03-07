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
import turtle
Anyturtle = turtle.Turtle()
l=30
w=60
def DrawRectange(Anyturtle, l, w):
    for i in range(2):
        Anyturtle.forward(l)
        Anyturtle.right(90)
        Anyturtle.forward(w)
        Anyturtle.right(90)

DrawRectange(Anyturtle, l, w)

input()
