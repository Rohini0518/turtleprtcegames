import colorgram
import turtle
import random

t=turtle.Turtle()
screen=turtle.Screen()
screen.colormode(255)

# colors = colorgram.extract('spotcolor.jpg', 6)
# print(colors)
# print(colors[0].rgb)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)    


rgb_Colors=[(255, 161, 149), (19, 78, 165), (236, 35, 108), (221, 231, 238), (145, 28, 66),(19, 78, 165), (179, 78, 165)]


def dot_xcolor():
    x_length=50
    for _ in rgb_Colors:
        colr=random.choice(rgb_Colors)
        t.dot(20, colr)
        t.teleport(x_length)
        x_length+=50
        
def dot_ycolor():     
    y_length=45    
    for _ in rgb_Colors:
        dot_xcolor()
        t.teleport(0,y_length)
        y_length+=45

dot_ycolor()
screen.exitonclick()
