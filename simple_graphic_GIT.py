# coding: utf-8

import turtle
import random


def color_selection(color):
    if not color:
        turtle.fillcolor(random.random(), random.random(), random.random())  # случайный выбор цвета для окружности
    else:
        turtle.fillcolor(color)  # заданный цвет окружности
answer = ''
while answer != 'n':
    answer = turtle.textinput("Draw a circle:", "y/n")
    if answer == 'y':
        radius = turtle.textinput("Draw a circle:", "Enter the diameter:")
        color = turtle.textinput("Draw a circle:", "Enter the color:")
        turtle.speed(0)
        turtle.penup()      # поднимаем перо
        turtle.goto(random.randrange(-100, 100), random.randrange(-100, 100))
        turtle.pendown()    # опускаем перо

        turtle.begin_fill() # в начале закрашиваемого объекта
        if not radius:
            turtle.circle(random.randrange(1, 100))
            color_selection(color)
        else:
            turtle.circle(int(radius))
            color_selection(color)
        turtle.end_fill()   # в конце закрашиваемого объекта