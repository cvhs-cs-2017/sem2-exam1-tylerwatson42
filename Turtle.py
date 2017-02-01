"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(90)
    t.left(90)
t.left(45)
t.forward(90)
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
input()

"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
