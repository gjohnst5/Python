import colorgram
import turtle as t
import random

#color gen
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     rgb_colors.append(color_tuple)
#
# print(rgb_colors)

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()

colors = [(58, 106, 148), (224, 200, 110), (134, 85, 59), (222, 139, 64), (195, 145, 171), (144, 179, 202), (139, 81, 104), (209, 91, 69), (68, 106, 90), (188, 80, 119), (135, 182, 137), (64, 156, 92), (47, 156, 193), (129, 134, 76), (183, 191, 201), (215, 177, 192), (20, 68, 114), (20, 59, 95), (174, 203, 181), (115, 123, 151), (229, 174, 165), (159, 205, 214), (70, 59, 48), (76, 63, 48), (121, 45, 57), (125, 44, 42)]

for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(40)
    if (i + 1) % 2 == 0:
        for _ in range(2):
            tim.left(90)
            tim.forward(40)
    else:
        for _ in range(2):
            tim.right(90)
            tim.forward(40)

screen = t.Screen()
screen.exitonclick()