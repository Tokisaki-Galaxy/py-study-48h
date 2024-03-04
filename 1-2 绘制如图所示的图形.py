#turtle任务一
from turtle import *
color("darkred","red")
shape("turtle")
pensize(3)
speed(100)

for i in range(5):
    begin_fill()
    circle(50)
    end_fill()
    left(60)

begin_fill()
circle(50,240)
end_fill()
left(60)

penup()
goto(0,0)
pendown()
setheading(0)
begin_fill()
circle(50,120)
end_fill()

penup()
goto(175,-125)
pendown()
write("2306020123 韩镒名",font=("Arial",20,"normal"))
hideturtle()
done()