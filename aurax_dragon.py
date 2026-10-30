
import turtle
import math
import random

# ==========================================
# AURAX | CRIMSON DRAGON
# Generative Fantasy Artwork
# ==========================================

screen = turtle.Screen()
screen.setup(1100, 900)
screen.bgcolor("#080609")
screen.title("AURAX | CRIMSON DRAGON")
screen.colormode(255)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

RED = "#D10B25"
DARK_RED = "#690817"
BRIGHT_RED = "#FF253F"
GOLD = "#FFC857"
DARK = "#14070D"
WHITE = "#FFF0E5"


# ==========================================
# DRAWING ENGINE
# ==========================================

def polygon(points, fill, outline=None, width=2):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.fillcolor(fill)
    pen.pencolor(outline or fill)
    pen.pensize(width)

    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


def line(points, color, width=2):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.pencolor(color)
    pen.pensize(width)

    for point in points[1:]:
        pen.goto(point)


def circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


def bezier(p0, p1, p2, p3, color, width=3):
    points = []

    for i in range(51):
        t = i / 50
        u = 1 - t

        x = (u**3 * p0[0] +
             3*u**2*t*p1[0] +
             3*u*t**2*p2[0] +
             t**3*p3[0])

        y = (u**3 * p0[1] +
             3*u**2*t*p1[1] +
             3*u*t**2*p2[1] +
             t**3*p3[1])

        points.append((x, y))

    line(points, color, width)


def mirror(points, side):
    return [(x * side, y) for x, y in points]


# ==========================================
# BACKGROUND
# ==========================================

random.seed(42)

# Decorative rings
for radius in [170, 185, 360, 375]:
    pen.penup()
    pen.goto(0, -radius)
    pen.pendown()
    pen.pencolor("#40101C")
    pen.pensize(1)
    pen.circle(radius)

# Background particles
for _ in range(180):
    x = random.randint(-520, 520)
    y = random.randint(-420, 420)
    size = random.choice([1, 2, 3])

    circle(x, y, size, random.choice([
        "#641020", "#A21A30", "#D14A42", "#54212A"
    ]))


# ==========================================
# DRAGON WINGS
# ==========================================

wing_points = [
    (55, 85),
    (115, 155),
    (190, 205),
    (285, 235),
    (245, 175),
    (350, 190),
    (290, 130),
    (385, 115),
    (290, 75),
    (355, 15),
    (245, 30),
    (205, -55),
    (145, -5),
    (90, -85),
    (65, 25)
]

for side in [-1, 1]:
    polygon(
        mirror(wing_points, side),
        DARK_RED,
        RED,
        3
    )

    # Wing bone structure
    wing_bones = [
        ((55, 85), (115, 155), (190, 205), (285, 235)),
        ((65, 25), (130, 55), (210, 120), (350, 190)),
        ((90, -85), (150, -15), (220, 15), (385, 115)),
        ((145, -5), (180, 20), (240, 30), (355, 15)),
        ((205, -55), (230, -15), (270, 5), (290, 75))
    ]

    for p0, p1, p2, p3 in wing_bones:
        bezier(
            tuple(v * side for v in p0),
            tuple(v * side for v in p1),
            tuple(v * side for v in p2),
            tuple(v * side for v in p3),
            "#F13A49",
            2
        )

    # Wing membrane details
    for i in range(5):
        y = 130 - i * 38
        x = 100 + i * 25

        bezier(
            (side * x, y),
            (side * (x + 45), y - 25),
            (side * (x + 85), y - 55),
            (side * (x + 135), y - 80),
            "#A51B30",
            2
        )


# ==========================================
# DRAGON BODY AND TAIL
# ==========================================

bezier(
    (0, -90),
    (-55, -175),
    (-80, -240),
    (-30, -320),
    RED, 22
)

bezier(
    (-30, -320),
    (25, -390),
    (130, -350),
    (155, -420),
    RED, 17
)

# Tail tip
polygon(
    [(135, -390), (185, -455), (145, -438),
     (155, -485), (110, -435)],
    DARK_RED,
    RED,
    3
)

# Body highlights
bezier(
    (-12, -110),
    (-65, -190),
    (-75, -245),
    (-25, -315),
    "#FF4A51", 3
)

bezier(
    (-25, -315),
    (30, -370),
    (105, -355),
    (150, -420),
    "#FF4A51", 3
)


# ==========================================
# NECK ARMOR
# ==========================================

polygon(
    [(-75, -60), (-105, -150), (-65, -235),
     (0, -280), (65, -235), (105, -150),
     (75, -60), (0, -105)],
    "#781020",
    RED,
    3
)

for i in range(5):
    y = -100 - i * 28
    polygon(
        [(-48, y), (0, y - 18), (48, y),
         (0, y - 35)],
        "#C52236",
        "#F34A50",
        1
    )


# ==========================================
# DRAGON HEAD
# ==========================================

# Main skull
polygon(
    [
        (-78, 125),
        (-100, 190),
        (-55, 235),
        (0, 255),
        (55, 235),
        (100, 190),
        (78, 125),
        (55, 70),
        (0, 35),
        (-55, 70)
    ],
    "#A10E23",
    "#F13B4C",
    3
)

# Face armor
for side in [-1, 1]:
    polygon(
        mirror([
            (8, 195), (35, 215), (75, 185),
            (65, 125), (30, 105), (12, 145)
        ], side),
        "#D51D34",
        "#FF5963",
        2
    )

# Horns
for side in [-1, 1]:
    bezier(
        (side * 52, 215),
        (side * 95, 275),
        (side * 105, 300),
        (side * 80, 340),
        "#E4B7A0", 10
    )

    bezier(
        (side * 78, 225),
        (side * 125, 250),
        (side * 145, 275),
        (side * 155, 315),
        "#B83240", 8
    )

# Snout
polygon(
    [
        (-55, 125), (-70, 85), (-40, 55),
        (0, 45), (40, 55), (70, 85),
        (55, 125), (0, 145)
    ],
    "#6C101D",
    "#E33A49",
    3
)

# Eyes
for side in [-1, 1]:
    polygon(
        mirror([
            (8, 175), (25, 193),
            (58, 185), (43, 163)
        ], side),
        GOLD,
        "#FFEEA5",
        2
    )

    circle(side * 35, 177, 5, "#1A0809")
    circle(side * 36, 179, 2, WHITE)

# Nostrils
for side in [-1, 1]:
    circle(side * 22, 90, 5, "#16060A")
    circle(side * 22, 91, 2, RED)

# Mouth
bezier(
    (-48, 65),
    (-25, 35),
    (25, 35),
    (48, 65),
    "#FF5963", 3
)

# Teeth
for side in [-1, 1]:
    polygon(
        mirror([
            (12, 61), (22, 43), (30, 62)
        ], side),
        WHITE,
        WHITE,
        1
    )

# Facial details
for side in [-1, 1]:
    bezier(
        (side * 60, 150),
        (side * 85, 130),
        (side * 90, 105),
        (side * 75, 90),
        "#FF6872", 3
    )


# ==========================================
# DECORATIVE SCALES
# ==========================================

for side in [-1, 1]:
    for row in range(4):
        for col in range(3):
            x = side * (30 + col * 16)
            y = 5 - row * 18

            polygon(
                [
                    (x, y + 7),
                    (x + side * 7, y),
                    (x, y - 8),
                    (x - side * 7, y)
                ],
                "#D52B40",
                "#FF5863",
                1
            )


# ==========================================
# FIRE PARTICLES
# ==========================================

for i in range(22):
    angle = math.radians(i * 360 / 22)

    x = 215 * math.cos(angle)
    y = 215 * math.sin(angle)

    circle(x, y, random.choice([2, 3, 4]), 
           random.choice([GOLD, BRIGHT_RED, "#FF8A43"]))


# ==========================================
# TITLE AND SIGNATURE
# ==========================================

pen.penup()
pen.goto(0, -535)
pen.pencolor("#F02B42")
pen.write(
    "A U R A X",
    align="center",
    font=("Georgia", 34, "bold")
)

pen.goto(0, -570)
pen.pencolor("#B88B65")
pen.write(
    "CRIMSON DRAGON",
    align="center",
    font=("Georgia", 11, "normal")
)

pen.goto(0, -600)
pen.pencolor("#6D3540")
pen.write(
    "WHERE LEGENDS ARE BORN",
    align="center",
    font=("Arial", 8, "normal")
)

# ==========================================
# FINAL RENDER
# ==========================================

screen.update()
turtle.done()
