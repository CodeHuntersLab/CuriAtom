from turtle import*
import turtle

setup(720,500,0,0)
dot(50,0,0,0)

a=turtle.Turtle()
a.shape("circle")
a.shapesize(15,4)
a.pencolor("red")
a.fillcolor("")

b=turtle.Turtle()
b.shape("circle")
b.shapesize(4,15)
b.pencolor("green")
b.fillcolor("")

c=turtle.Turtle()
c.penup()
c.right(45)
c.pendown()
c.shape("circle")
c.shapesize(4,15)
c.pencolor("orange")
c.fillcolor("")

d=turtle.Turtle()
d.penup()
d.left(45)
d.pendown()
d.shape("circle")
d.shapesize(4,15)
d.pencolor("blue")
d.fillcolor("")

e=turtle.Turtle()
e.penup()
e.left(45)
e.forward(150)
e.pendown()
e.write("          Atomo")

turtle.exitonclick()




