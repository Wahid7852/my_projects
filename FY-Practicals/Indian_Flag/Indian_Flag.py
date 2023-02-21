import os
import turtle

from turtle import *
os.system('cls')

Screen = turtle.Screen()

t=turtle.Turtle()
t.speed(0)

t.penup()
t.goto(-400, 250)
t.pendown()
print("initial position is: ", t.pos())

#orange
t.color('#FF9933')
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
print("position of orange block is: ", t.pos())

#block change
t.left(90)
t.color('#FFFFFF')
t.forward(167)
print("position of block change is: ", t.pos())

#green
t.color('#138808')
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()
print("position of green block is: ", t.pos())

#white strip and ashoka chakra
t.penup()
t.goto(70, 0)
t.pendown()
t.color('#000080')
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(60, 0)
t.pendown()
t.color('#FFFFFF')
t.begin_fill()
t.circle(60)
t.end_fill()
 
t.penup()
t.goto(-57, -8)
t.pendown()
t.color('#000080')

for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()
     
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)

turtle.done()