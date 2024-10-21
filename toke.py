import turtle as trtl
import random
import math

class Scenery:
    def __init__(self, loco):
        self.loco = loco
        self.turtle = trtl.Turtle()
        self.screen = trtl.Screen()
        self.turtle.speed(0)
        self.draw_scenery()
        self.done_drawing()

    def draw_gradient_sky(self):
        colors = ["#FF8C00", "#FF6B00", "#FF4500", "#FF1493", "#4B0082"] # color list 
        height = 800
        section_height = height / len(colors)

        for i, color in enumerate(colors):
            self.turtle.penup()
            self.turtle.goto(-600, 400 - (i * section_height))    #Make a series of coordinate such that the function can execute at these points 
            self.turtle.setheading(0)
            self.turtle.fillcolor(color)
            self.turtle.begin_fill()
            for _ in range(2):
                self.turtle.forward(1200)
                self.turtle.right(90)
                self.turtle.forward(section_height)
                self.turtle.right(90)
            self.turtle.end_fill()

    def draw_sun(self):
        """Draw the setting sun"""
        self.turtle.penup()
        self.turtle.goto(0, 50)
        self.turtle.fillcolor("#FFD700") #using set colors to fill in the sun
        self.turtle.begin_fill()
        self.turtle.circle(60)
        self.turtle.end_fill()

        self.turtle.penup()
        self.turtle.goto(0, 40)
        self.turtle.setheading(270)
        self.turtle.pensize(2)
        self.turtle.pencolor("#FFD700")

        for _ in range(30):
            self.turtle.penup()
            self.turtle.goto(random.randint(-50, 50), 40)
            self.turtle.pendown()
            self.turtle.forward(random.randint(100, 200))

    def draw_ocean(self):
        """Draw ocean with waves"""
        self.turtle.penup()
        self.turtle.goto(-600, 50)
        self.turtle.fillcolor("#4169E1") # Making waves color set to this 
        self.turtle.begin_fill()
        self.turtle.setheading(0)

        amplitude = 20
        frequency = 0.02
        x = -600
        while x < 600:
            y = amplitude * math.sin(frequency * x) + 50 # Making the shape of the waves as they corrospond to the shape of a sin graph
            self.turtle.goto(x, y)
            x += 10
            if x == -590:
                self.turtle.pendown()

        self.turtle.goto(600, -400)
        self.turtle.goto(-600, -400)
        self.turtle.goto(-600, 50)
        self.turtle.end_fill()

    def draw_sand(self):
        """Draw beach sand"""
        self.turtle.penup()
        self.turtle.goto(-600, -50)
        self.turtle.fillcolor("#F0E68C")
        self.turtle.begin_fill()
        self.turtle.setheading(0)
        self.turtle.forward(1200)
        self.turtle.right(90)
        self.turtle.forward(350)
        self.turtle.right(90)
        self.turtle.forward(1200)
        self.turtle.right(90)
        self.turtle.forward(350)
        self.turtle.end_fill()

    def draw_building(self, x, height):
        self.turtle.penup()
        self.turtle.goto(x, -200)
        self.turtle.setheading(0)
        self.turtle.pendown()

        # Draw building outline
        self.turtle.fillcolor('gray20')
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.forward(60)
            self.turtle.left(90)
            self.turtle.forward(height)
            self.turtle.left(90)
        self.turtle.end_fill()

        window_rows = height // 40
        window_cols = 3
        window_width = 10
        window_height = 15
        start_x = x + 10

        for row in range(window_rows):
            for col in range(window_cols):
                self.turtle.penup()
                window_x = start_x + (col * 20)
                window_y = -180 + (row * 40)
                self.turtle.goto(window_x, window_y)

                window_color = 'yellow' if random.random() > 0.4 else 'black'
                self.turtle.fillcolor(window_color)

                self.turtle.begin_fill()
                for _ in range(2):
                    self.turtle.forward(window_width)
                    self.turtle.left(90)
                    self.turtle.forward(window_height)
                    self.turtle.left(90)
                self.turtle.end_fill()

    def draw_skyline(self):
        self.screen.bgcolor("dark blue")
        self.turtle.penup()
        for _ in range(50):
            x = random.randint(-600, 600)
            y = random.randint(0, 400)
            self.turtle.goto(x, y)
            self.turtle.dot(2, 'white')

        x_position = -600
        while x_position < 600:
            height = random.randint(100, 400)
            self.draw_building(x_position, height)
            x_position += 60

        self.turtle.penup()
        self.turtle.goto(-600, -200)
        self.turtle.fillcolor('gray10')
        self.turtle.begin_fill()
        self.turtle.setheading(0)
        for _ in range(2):
            self.turtle.forward(1200)
            self.turtle.right(90)
            self.turtle.forward(100)
            self.turtle.right(90)
        self.turtle.end_fill()


    def house(self):
        self.screen.bgcolor("light blue")
        painter = trtl.Turtle()
        painter.speed(100)
        painter.penup()
        painter.left(180)
        painter.forward(170)
        painter.right(90)
        painter.forward(180)
        painter.pendown()
        painter.fillcolor("yellow")
        painter.begin_fill()
        painter.circle(70)
        painter.end_fill()
        painter.penup()
        painter.right(180)
        painter.forward(200)
        painter.left(90)
        painter.forward(100)
        painter.pendown()
        painter.fillcolor("beige")
        painter.begin_fill()
        painter.right(90)
        painter.forward(100)
        painter.right(90)
        painter.forward(100)
        painter.right(90)
        painter.forward(100)
        painter.right(90)
        painter.forward(100)
        painter.end_fill()
        painter.fillcolor("brown")
        painter.begin_fill()
        painter.left(115)
        painter.forward(100)
        painter.left(122)
        painter.forward(110)
        painter.end_fill()

    def space(self):
        self.screen.bgcolor("black")
        self.turtle.pencolor("white")
        for i in range(30):
            self.turtle.penup()
            self.turtle.goto((random.randint(-1000,1000), random.randint(-500,500)))
            self.turtle.pendown()
            for e in range(5):
                self.turtle.forward(30)
                self.turtle.right(144)
    def draw_person(self):
        p = trtl.Turtle()
        p.goto(200,0)
        p.pensize(2)
        p.speed(0)

        p.fillcolor("red")
        p.begin_fill()
        p.left(45)
        p.circle(30, 270)
        loco = p.pos()
        p.heading()
        p.penup()
        p.goto(200, 0)
        p.pendown()
        p.left(90)
        p.forward(60)
        p.right(90)
        p.circle(5, 270)
        p.forward(50)

        p.penup()
        p.goto(loco)
        p.pendown()
        p.setheading(0)
        p.left(130)
        p.forward(60)
        p.left(90)
        p.circle(-5, 270)
        p.forward(50)

        p.right(40)
        p.forward(100)
        p.right(15)
        p.forward(60)
        p.right(90)
        p.circle(5, 270)
        p.forward(50)

        p.setheading(0)
        p.forward(50)

        p.penup()
        p.forward(5)
        p.pendown()
        loco = p.pos()

        p.right(45)
        p.forward(60)
        p.left(90)
        p.circle(-5, 270)
        p.forward(70)

        p.penup()
        p.goto(loco)
        p.pendown()
        p.setheading(0)
        p.left(90)
        p.forward(100)
        p.end_fill()

    def draw_scenery(self):
        if self.loco == "Beach" or self.loco == "Beache":
            self.draw_gradient_sky()
            self.draw_ocean()
            self.draw_sand()
            self.draw_sun()
            self.draw_person()
        if self.loco == "Skyline":
            self.draw_skyline()
            self.draw_person()
        if self.loco == "House":
            self.house()
            self.draw_person()
        if self.loco == "Space":
            self.space()
            self.draw_person()

    def done_drawing(self):
        wn = trtl.Screen()
        wn.mainloop()
def main():
    imageList = ["skyline", "beach", "house", "space"]
    # inputNumber, imageType = prompt(imageList)
    imageType = prompt(imageList)


    Scenery(loco=imageType)


def prompt(imageList):
    sourceInput = input("Hi, you could create a small story about a person in different locations(space, beach, house, skyline) What would you like to generate: ").lower().strip()

    # Split the input into words
    words = sourceInput.split()

    # Extract numerical options
    numericalOptions = [int(word) for word in words if word.isdigit()]

    # Extract item options (words that are not numbers)
    itemOptions = [word for word in words if word.isalpha()]

    # Find the final item and number
    finalItem = itemMatching(itemOptions, imageList)

    # if len(numericalOptions) > 1:
    #     finalNum = numberSelector(sourceInput, numericalOptions, finalItem)
    # elif len(numericalOptions) == 0:
    #     finalNum = 1
    # else:
    #     finalNum = numericalOptions[0]

    print(["I am drawing " + finalItem])
    return finalItem


def itemMatching(imageList, allowedItems):
    # Normalize allowed items for comparison
    allowedItems_normalized = [item.lower() for item in allowedItems]

    pluralItems = ["beaches", "skylines", "houses", "spaces"]

    for item in imageList:
        # Normalize item for comparison
        normalized_item = item.lower()
        if normalized_item in allowedItems_normalized:
            return normalized_item.capitalize()
        elif normalized_item in pluralItems:
            return normalized_item[:-1].capitalize()


    return None


def numberSelector(input, numberList, item):
    finalNumSelector = (None, float('inf'))

    if item is None:
        return 1

    item_index = input.find(item.lower())

    for n in numberList:
        number_index = input.find(str(n))
        if number_index != -1:
            proximity = abs(item_index - number_index)
            if proximity < finalNumSelector[1]:
                finalNumSelector = (n, proximity)

    return finalNumSelector[0] if finalNumSelector[0] is not None else 1


def verifyNum(inputMessage):
    while True:
        num = input(inputMessage)
        if num.isdigit():
            return int(num)
        else:
            print("Please make it a number")


def guidelines():
    print("Sorry, nothing you have given us follows community guidelines")
    prompt([])  # Pass an empty list to avoid recursion with an undefined itemList


if __name__ == "__main__":
    main()
