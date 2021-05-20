
import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
turtle.bgcolor("black")

t1.color("red")
t2.color("blue")
t3.color("#123456")
t4.color("green")

dis = 20
for t in [t2, t3, t4]:
    t.penup()
    t.left(90)
    t.forward(dis)
    t.right(90)
    t.pendown()
    dis += 20

for i in range(10):
    for t in [t1, t2, t3, t4]:
        t.forward(random.randint(10, 40))
turtle.exitonclick()
