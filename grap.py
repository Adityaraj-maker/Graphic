from turtle import*
import turtle

turtle.bgcolor("black")
turtle.pensize("2")
color("cyan")
begin_fill()
while(True):
    forward(200)
    left(170)
    if abs (pos()) <1:
        break