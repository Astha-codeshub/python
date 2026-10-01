import turtle
import math
import colorsys

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#040008")
screen.title("Quantum Love")

# ---------------- MAIN TURTLE ----------------
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

# ---------------- DRAW HEART ----------------
def heart_point(t, scale=12):
    points = []

    for degree in range(0, 360, 2):
        angle = math.radians(degree)

        # Parametric heart equation
        x = 16 * math.sin(angle) ** 3
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )

        points.append((x * scale, y * scale))

    return points


# ---------------- GLOWING HEART ----------------
points = heart_point(t, 12)

# Draw several hearts to create a glowing effect
for layer in range(8, 0, -1):

    hue = (layer / 8) * 0.95
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    # Convert RGB values to 0-255
    color = tuple(int(c * 255) for c in color)

    t.color(color)
    t.width(layer)

    t.penup()
    t.goto(points[0])
    t.pendown()

    for x, y in points:
        t.goto(x, y)


# ---------------- QUANTUM RINGS ----------------
for ring in range(6):

    radius = 180 + ring * 35

    hue = (ring / 6) * 0.9
    color = colorsys.hsv_to_rgb(hue, 0.8, 1.0)

    color = tuple(int(c * 255) for c in color)

    t.color(color)
    t.width(2)

    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()

    t.circle(radius)


# ---------------- CENTER DOT ----------------
t.penup()
t.goto(0, 0)
t.dot(18, "#ffffff")

# ---------------- SMALL PARTICLES ----------------
for i in range(60):

    angle = math.radians(i * 37)
    radius = 250 + (i % 5) * 25

    x = math.cos(angle) * radius
    y = math.sin(angle) * radius

    hue = (i / 60) % 1.0
    color = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
    color = tuple(int(c * 255) for c in color)

    t.penup()
    t.goto(x, y)
    t.dot(4, color)


# ---------------- FINISH ----------------
screen.update()
turtle.done()