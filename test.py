import turtle
import random

screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.setup(width=800, height=600)
screen.title("Colorful Polygons")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

fill_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
border_colors = ["white", "lightgray", "gold", "skyblue", "pink"]

def draw_fancy_polygon(sides, length):
    fill_color = random.choice(fill_colors)
    border_color = random.choice(border_colors)

    pen.fillcolor(fill_color)
    pen.pencolor(border_color)
    pen.pensize(3)

    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
    pen.end_fill()

def random_position():
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    return x, y

num_triangles = 10
num_rectangles = 8
num_hexagons = 6

for _ in range(num_triangles):
    pen.penup()
    x, y = random_position()
    pen.goto(x, y)
    pen.pendown()
    draw_fancy_polygon(3, random.randint(50, 100))

for _ in range(num_rectangles):
    pen.penup()
    x, y = random_position()
    pen.goto(x, y)
    pen.pendown()
    draw_fancy_polygon(4, random.randint(60, 120))

for _ in range(num_hexagons):
    pen.penup()
    x, y = random_position()
    pen.goto(x, y)
    pen.pendown()
    draw_fancy_polygon(6, random.randint(40, 80))

star = turtle.Turtle()
star.speed(0)
star.hideturtle()
star.color("yellow")

for _ in range(50):
    star.penup()
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    for _ in range(5):
        star.forward(5)
        star.right(144)
    star.end_fill()

screen.update()
turtle.done()
