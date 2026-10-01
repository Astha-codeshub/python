import turtle
import sys
import math
import colorsys

screen=turtle.Screen()
screen.setup(width=950,height=950)
screen.bgcolor("#000804")
screen.title("Quantum Love")
turtle.tracer(3)

#Turtle setup
t=turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

#secondary turtle setup
hud=turtle.Turtle()
hud.speed(0)
hud.hideturtle()
hud.penup()

#configuration variables
is_paused=False
heart_beat_speed=3.0
num_rings=18
twistfactor=1.2
manifold_mode=0
palette_idx=0
camera_distance=420.0
master_time=0.0
rot_x=0.0
rot_y=0.0
rot_z=0.0

t.penup()
t.goto(0 , -100)
t.pendown()

for i in range(36):
    color=colorsys.hsv_to_rgb(i/36, 0.8 ,1.0)
    t.pencolor(color)
    t.circle(100)
    t.right(10)
    screen.update()

turtle.done()