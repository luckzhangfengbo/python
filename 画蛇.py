#!/usr/bin/env python
# coding=utf-8
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(10)
turtle.pencolor("yellow")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
