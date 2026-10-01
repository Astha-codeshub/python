import turtle
import math
import colorsys

# Setup screen
screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#040008")
screen.title("Quantum Love")
turtle.tracer(3)

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Set color mode to 1.0 (default for colorsys output)
turtle.colormode(1.0)


# Heart point generation function
def heart_point(scale=12):
    points = []
    # Loop through angles in radians from 0 to 2*pi
    for i in range(360):
        angle = math.radians(i)
        x = 16 * (math.sin(angle) ** 3)
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )
        points.append((x * scale, y * scale))
    return points


# Generate main heart path points
points = heart_point(12)

# Draw several heart layers to create a glowing effect
for layer in range(8, 0, -1):
    hue = (layer / 8) * 0.95
    # colorsys returns float tuples (R, G, B) in range 0.0 to 1.0
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    t.pencolor(color)
    t.penup()

    # Move to starting point of the layer
    start_x, start_y = points[0]
    t.goto(start_x * (layer / 8), start_y * (layer / 8))
    t.pendown()

    for x, y in points:
        t.goto(x * (layer / 8), y * (layer / 8))

    screen.update()

turtle.done()