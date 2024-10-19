import turtle
import math
from random import randint



screen = turtle.Screen()
screen.setup(1200, 800)
screen.title("Beach Sunset")
screen.tracer(0)  


t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def draw_gradient_sky():

    colors = ["#FF8C00", "#FF6B00", "#FF4500", "#FF1493", "#4B0082"]
    height = 800
    section_height = height / len(colors)
   
    for i, color in enumerate(colors):
        t.penup()
        t.goto(-600, 400 - (i * section_height))
        t.setheading(0)
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(2):
            t.forward(1200)
            t.right(90)
            t.forward(section_height)
            t.right(90)
        t.end_fill()


def draw_sun():
    """Draw the setting sun"""
    t.penup()
    t.goto(0, 50)
    t.fillcolor("#FFD700")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
   
    t.penup()
    t.goto(0, 40)
    t.setheading(270)
    t.pensize(2)
    t.pencolor("#FFD700")
   
    for _ in range(30):
        t.penup()
        t.goto(randint(-50, 50), 40)
        t.pendown()
        t.forward(randint(100, 200))


def draw_palm_tree(x, y):
    """Draw a palm tree at specified location"""
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pensize(20)
    t.pencolor("#8B4513")
    t.pendown()
    t.forward(150)
   
    leaf_positions = [(40, 30), (-40, 30), (60, 0), (-60, 0), (30, -30), (-30, -30)]
    for angle, length in leaf_positions:
        t.penup()
        t.goto(x, y + 150)
        t.setheading(90 + angle)
        t.pencolor("#228B22")
        t.pensize(8)
        t.pendown()
        t.forward(100)


def draw_sand():
    """Draw beach sand"""
    t.penup()
    t.goto(-600, -50)
    t.fillcolor("#F0E68C")
    t.begin_fill()
    t.setheading(0)
    t.forward(1200)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(1200)
    t.right(90)
    t.forward(350)
    t.end_fill()


def draw_ocean():
    """Draw ocean with waves"""
    t.penup()
    t.goto(-600, 50)
    t.fillcolor("#4169E1")
    t.begin_fill()
    t.setheading(0)
   
    amplitude = 20
    frequency = 0.02
    x = -600
    while x < 600:
        y = amplitude * math.sin(frequency * x) + 50 # We are using a sin function to create the wave pattern of the ocean. Amplitude says how tall the ocean will be. Frequency says how many waves there are. 50 is to shift the waves of the ocean by 50 units. X=-600. Moves right 10 all the way till it reaches 601. And it will create a new y coordinate within the sin graph to make the waves correct as explained earlier. 
        t.goto(x, y)
        x += 10
        if x == -590:  
            t.pendown()
   
    t.goto(600, -400)
    t.goto(-600, -400)
    t.goto(-600, 50)
    t.end_fill()


def add_details():
    """Add birds and clouds"""
    for _ in range(5):
        x = randint(-500, 500)
        y = randint(200, 350)
        t.penup()
        t.goto(x, y)
        t.pencolor("black")
        t.pensize(2)
        t.setheading(0)
       
        
        t.pendown()
        t.left(45)
        t.forward(20)
        t.backward(20)
        t.right(90)
        t.forward(20)


def main():
    draw_gradient_sky()
    draw_ocean()
    draw_sand()
    draw_sun()
   
    palm_positions = [(-400, -50), (-200, -50), (200, -50), (400, -50)]
    for x, y in palm_positions:
        draw_palm_tree(x, y)
   
    add_details()
    screen.update()


main()
screen.tracer(1)
screen.mainloop()
