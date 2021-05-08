#!/usr/bin/python3
import turtle
import random 
window = turtle.Screen()
alex = turtle.Turtle()
window.bgcolor("black")
colors = ("red", "wheat", "green", "cyan", "yellow")
alex.speed(0)
arc = 50
scale = 8 
sweep = 2
slew = 2
spike = 123
alex.ht()
alex.color(random.choice(colors))

while True:
    for i in range(arc):
        alex.forward(scale)
        alex.right(sweep)
       
    alex.right(random.randint(spike-slew, spike + slew))

window.mainloop()
