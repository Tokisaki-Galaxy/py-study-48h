#turtle任务一
from turtle import *
pencolor("red")
shape("turtle")
pensize(3)

for i in range(3):
    circle(50)
    circle(-50)
    left(60)

penup()
goto(175,-125)
pendown()
write("xxxxxx",font=("Arial",20,"normal"))
hideturtle()