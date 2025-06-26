# task2_pythagoras_tree.py

import turtle
import math

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def pythagoras_tree(t, size, level):
    if level == 0:
        return
    draw_square(t, size)

    t.forward(size)
    t.left(45)
    new_size = size / math.sqrt(2)
    pythagoras_tree(t, new_size, level - 1)

    t.right(45)
    t.backward(size)

    t.left(90)
    t.forward(size)
    t.right(135)
    pythagoras_tree(t, new_size, level - 1)

    t.left(135)
    t.backward(size)
    t.right(90)

def draw_pythagoras_tree(level):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    pythagoras_tree(t, 100, level)
    screen.mainloop()
