#p1
color_list = ["red", "green", "pastel"]

print("color list:")
print(','.join(color_list))
#p2
new_color = input("Input a new color:")

color_list.append(new_color)
print("New color list:")
print(','.join(color_list))

position = int(input("Input position:"))
print(f"Color at position {position}:{color_list[position -1]}")
item_to_delete = input("Item to delete:")
if item_to_delete.isdigit():
    color_list.pop(int(item_to_delete)-1)
else:
    color_list.remove(item_to_delete)
print("New color list")
print(','.join(color_list))

import turtle
screen = turtle.Screen()
pen = turtle.Turtle()

for color in color_list:
    pen.color(color)
    pen.forward(100)
    pen.penup()
    pen.forward(10)
    pen.pendown()

screen.mainloop()

