import turtle
from turtle import Turtle, Screen
from getcolors import get_colors
from movecolors import move_colors
import colorgram

colors = colorgram.extract('image.jpg', 20)
real_colors = get_colors(colors, 4, 20)

turtle.colormode(255)
tim = Turtle()

move_colors(tim, 200, 200, 10, 20, real_colors)

screen = Screen()
screen.exitonclick()
