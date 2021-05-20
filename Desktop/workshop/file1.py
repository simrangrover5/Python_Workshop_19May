
import turtle

pen = turtle.Pen()
pen.color("red", "blue")
pen.begin_fill()

for i in range(1, 5):  # i --> 1, 2, 3, 4
    if i%2 == 0:
        pen.forward(200)
    else:
        pen.forward(100)
    pen.left(90)
pen.end_fill()
turtle.exitonclick()
