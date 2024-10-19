import turtle
import random


screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("City Skyline")
screen.setup(1200, 800)


t = turtle.Turtle()
t.speed(0) 
t.hideturtle()


def draw_building(x, height):
    t.penup()
    t.goto(x, -200) 
    t.setheading(0)
    t.pendown()
   
    # Draw building outline
    t.fillcolor('gray20')
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
   
    window_rows = height // 40
    window_cols = 3
    window_width = 10
    window_height = 15
    start_x = x + 10
   
    for row in range(window_rows):
        for col in range(window_cols):
            t.penup()
            window_x = start_x + (col * 20)
            window_y = -180 + (row * 40)
            t.goto(window_x, window_y)
           
            window_color = 'yellow' if random.random() > 0.4 else 'black'
            t.fillcolor(window_color)
           
            t.begin_fill()
            for _ in range(2):
                t.forward(window_width)
                t.left(90)
                t.forward(window_height)
                t.left(90)
            t.end_fill()


def draw_skyline():
  
    t.penup()
    for _ in range(50):
        x = random.randint(-600, 600)
        y = random.randint(0, 400)
        t.goto(x, y)
        t.dot(2, 'white')
   
   
    t.penup()
    t.goto(-500, 200)
    t.fillcolor('light yellow')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
   
    x_position = -600
    while x_position < 600:
        height = random.randint(100, 400)
        draw_building(x_position, height)
        x_position += 60
   
    t.penup()
    t.goto(-600, -200)
    t.fillcolor('gray10')
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(1200)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()


screen.tracer(0)  
draw_skyline()
screen.tracer(1)  
screen.mainloop()
