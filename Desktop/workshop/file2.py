
import turtle
import random 

def get_color():
    l = list("abcdef1234567890")
    return "#" + "".join([random.choice(l) for i in range(6)])

pen = turtle.Pen()
turtle.bgcolor("black")
pen.speed(0)
#pen.begin_fill()

for i in range(300):  # i --> 0 to 299
    pen.pencolor(get_color())
    pen.forward(i)
    pen.left(59)
#pen.end_fill()
turtle.exitonclick()
