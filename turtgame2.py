import turtle
import random


t=turtle.Turtle()
scrn=turtle.Screen()
turtle.colormode(255)

# this a random color function can use to get a random color that are in turtle
def rand_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

directions=[0,90,180,270]

# this is a random walk function, by running this pointer will moves in random direction
def random_walk():
    for _ in range(100):
        t.pensize(3)
        t.forward(25)
        t.setheading(random.choice(directions))
        t.color(rand_color())
  
t.speed(0)
random_walk()
t.pensize(1)
def draw_spirograph(angle):
    for _ in range(int(360/angle)):
        t.circle(60,360)  
        t.color(rand_color())
        t.left(angle)
draw_spirograph(10)  

  


scrn.exitonclick()