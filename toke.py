import turtle as trtl


class Flower:
    spacer = 0

    def __init__(self, num_petals, num_flowers, type_of_flower, spacing=100):
        self.num_petals = num_petals
        self.num_flowers = num_flowers
        self.type_of_flower = type_of_flower
        self.spacing = spacing
        self.turtle = trtl.Turtle()
        self.speed()
        self.draw_flower1()
        self.done_drawing()

    def speed(self):
        self.turtle.speed(10)  # Reduced speed for better visualization

    def draw_flower1(self):
        for i in range(self.num_flowers):
            self.draw_flower()
            self.turtle.color("black")
            self.turtle.pensize(1)
            self.turtle.setheading(0)
            self.turtle.penup()
            self.turtle.forward(self.spacing)
            self.turtle.pendown()

    def draw_flower(self):
        if self.type_of_flower == "Sunflower":
            pencolor = "yellow"
            petalcolor = "yellow"
        elif self.type_of_flower == "Rose":
            petalcolor = "red"
            pencolor = "beige"
        elif self.type_of_flower == "Lily":
            petalcolor = "pink"
            pencolor = "light pink"
        elif self.type_of_flower == "Lotus":
            petalcolor = "red"
            pencolor = "pink"
        elif self.type_of_flower == "Tulip":
            petalcolor = "purple"
            pencolor = "pink"
        else:
            pencolor = "black"
            petalcolor = "gray"

        self.turtle.penup()
        self.turtle.goto(-500 + Flower.spacer, 0)
        Flower.spacer += 250
        self.turtle.pendown()

        self.turtle.right(90)
        self.turtle.forward(160)
        self.turtle.left(90)

        self.turtle.fillcolor("green")
        self.turtle.begin_fill()
        self.turtle.left(90)
        self.turtle.forward(230)
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.right(90)
        self.turtle.forward(230)
        self.turtle.right(90)
        self.turtle.forward(5)
        self.turtle.end_fill()
        self.turtle.penup()
        self.turtle.back(2.5)
        self.turtle.right(90)
        self.turtle.forward(230)
        self.turtle.pendown()

        self.turtle.left(30)
        for _ in range(self.num_petals):
            self.turtle.pencolor(pencolor)
            self.turtle.fillcolor(petalcolor)
            self.turtle.begin_fill()
            self.turtle.pensize(6)
            self.turtle.circle(30)
            self.turtle.right(360 / self.num_petals)
            self.turtle.end_fill()
        self.turtle.setheading(0)
        self.turtle.right(90)
        self.turtle.forward(30)
        self.turtle.left(90)

        if self.type_of_flower == "Sunflower":
            self.turtle.fillcolor("brown")
            self.turtle.begin_fill()
            self.turtle.circle(30)
            self.turtle.end_fill()

    def done_drawing(self):
        wn = trtl.Screen()
        wn.mainloop()


def main():
    imageList = ["jumpingman", "dog", "punchingman", "dancingman"]
    inputNumber, imageType = prompt(imageList)

    flower_batch = Flower(num_petals=6, num_flowers=inputNumber, type_of_flower=imageType, spacing=100)


def prompt(itemList):
    sourceInput = input("Hi, what would you like to generate: ").lower().strip()

    # Split the input into words
    words = sourceInput.split()

    # Extract numerical options
    numericalOptions = [int(word) for word in words if word.isdigit()]

    # Extract item options (words that are not numbers)
    itemOptions = [word for word in words if word.isalpha()]

    # Find the final item and number
    finalItem = itemMatching(itemOptions, itemList)

    if len(numericalOptions) > 1:
        finalNum = numberSelector(sourceInput, numericalOptions, finalItem)
    elif len(numericalOptions) == 0:
        finalNum = 1
    else:
        finalNum = numericalOptions[0]

    print([finalNum, finalItem])
    return finalNum, finalItem


def itemMatching(itemList, allowedItems):
    # Normalize allowed items for comparison
    allowedItems_normalized = [item.lower() for item in allowedItems]

    pluralItems = ["jumpingmen", "dogs", "punchingmen", "dancingmen"]

    for item in itemList:
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
