#more experiences with turtle
import turtle

draw = turtle.Turtle()

draw.speed(100)

for i in range(180):
    draw.forward(100)
    draw.right(30)
    draw.forward(20)
    draw.left(60)
    draw.forward(50)
    draw.right(30)

    draw.penup()
    draw.setposition(0, 0)
    draw.pendown()

    draw.right(2)

for i in range(200):
    draw.goto(0,-300)
    draw.forward(100)
    draw.left(123)


turtle.done()
