#learning to draw using turtle!

import turtle

draw = turtle.Turtle()
draw.speed(10)

lines = 1000
draw.penup()
draw.goto(-500,-100)
draw.pendown()

for i in range (1,101):
   draw.forward(lines)
   draw.left(190)
   lines = lines - 4
