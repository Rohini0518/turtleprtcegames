import  turtle
import random
t=turtle.Turtle()
scrn=turtle.Screen()
colors=["red","green","blue","cyan","purple","pink","salmon","indigo"]
degress=[120,90,72,60,51.43,45,40,36]
shapes=[3,4,5,6,7,8,9,10]

def draw():
    for p in range(len(shapes)) :
        for _ in range(shapes[p]):
            # r=shapes[p]
            t.color(colors[p])
            t.right(degress[p])
            t.pensize(4)
            t.forward(100)

draw()

def draw_shapes(angle_num):
    for _ in range(angle_num):
        t.left(360/angle_num)
        t.forward(100)

for i in range(3,11):
    t.color(random.choice(colors))
    t.speed(8)
    draw_shapes(i)
    

for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()



scrn.exitonclick()