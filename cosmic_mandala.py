
import turtle
import math
import colorsys

# ==============================
# CONFIGURAÇÕES
# ==============================

screen = turtle.Screen()
screen.colormode(255)
screen.setup(1000, 850)
screen.bgcolor("#080817")
screen.title("COSMIC MANDALA | Generative Art")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(1)

def neon_color(hue, saturation=0.85, value=1):
    rgb = colorsys.hsv_to_rgb(hue % 1, saturation, value)
    return tuple(int(c * 255) for c in rgb)

# ==============================
# FUNÇÕES DE DESENHO
# ==============================

def draw_circle(radius, color, width=1):
    pen.pensize(width)
    pen.pencolor(color)
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pendown()
    pen.circle(radius)

def draw_polygon(radius, sides, rotation, color):
    pen.pencolor(color)
    pen.pensize(1)
    pen.penup()

    points = []

    for i in range(sides):
        angle = math.radians(rotation + i * 360 / sides)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))

    pen.goto(points[0])
    pen.pendown()

    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])

def draw_petals(radius, petals, rotation, color):
    pen.pencolor(color)
    pen.pensize(1)

    for i in range(petals):
        angle = rotation + i * 360 / petals

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.forward(radius / 2)
        pen.pendown()

        pen.circle(radius / 2, 90)
        pen.left(90)
        pen.circle(radius / 2, 90)

def draw_spokes(radius, count, color):
    pen.pencolor(color)

    for i in range(count):
        angle = i * 360 / count

        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.pendown()
        pen.forward(radius)

# ==============================
# ESTRELAS DECORATIVAS
# ==============================

def draw_stars(amount):
    import random

    random.seed(42)

    for _ in range(amount):
        x = random.randint(-480, 480)
        y = random.randint(-400, 400)
        size = random.choice([1, 2, 3])

        pen.penup()
        pen.goto(x, y)
        pen.dot(size, random.choice([
            "#FFFFFF", "#8DEBFF",
            "#C59AFF", "#FF9BEA"
        ]))

# ==============================
# CONSTRUÇÃO DA ARTE
# ==============================

draw_stars(350)

# Anéis externos
for i in range(12):
    radius = 100 + i * 22
    hue = 0.48 + i * 0.025
    color = neon_color(hue)

    draw_circle(radius, color, 1)

# Geometria hexagonal
for i in range(8):
    radius = 130 + i * 22
    hue = 0.75 + i * 0.035

    draw_polygon(
        radius,
        6,
        i * 7.5,
        neon_color(hue)
    )

# Pétalas centrais
for i in range(5):
    radius = 110 + i * 28
    color = neon_color(0.78 + i * 0.055)

    draw_petals(radius, 16, i * 11, color)

# Raios luminosos
draw_spokes(320, 64, "#345BBA")

# Pequenos círculos ornamentais
for i in range(64):
    angle = math.radians(i * 360 / 64)
    x = 320 * math.cos(angle)
    y = 320 * math.sin(angle)

    pen.penup()
    pen.goto(x, y)
    pen.dot(5, neon_color(i / 64))

# Núcleo central
for radius in [70, 55, 40, 25, 12]:
    draw_circle(radius, "#72F5FF", 2)

# Centro luminoso
pen.penup()
pen.goto(0, 0)
pen.dot(16, "#FFFFFF")

# Detalhes finais
for i in range(32):
    angle = math.radians(i * 360 / 32)

    x = 370 * math.cos(angle)
    y = 370 * math.sin(angle)

    pen.penup()
    pen.goto(x, y)
    pen.dot(4, "#D59BFF")

screen.update()
turtle.done()
