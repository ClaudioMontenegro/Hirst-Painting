import random

def move_colors(name, x, y, number, dotsize,colors):
    """
    Function to make a dot painting using turtle module
    :param name: turtle object
    :param x: x-axis position
    :param y: y-axis position
    :param number: number of desired x and y dots
    :param colors: list of colors to randomly use
    :return:
    """
    x = -abs(x)
    y = -abs(y)
    for n in range(number):
        name.ht()
        name.penup()
        name.goto(x, y)
        name.st()
        name.shape("circle")
        for i in range(number):
            name.pendown()
            name.dot(dotsize, random.choice(colors))
            name.penup()
            name.forward(50)
        y += 50
    name.ht()
