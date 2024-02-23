from turtle import *

# direction
right(90)
forward(100)

right(90)
forward(100)

right(90)
forward(100)

right(90)
forward(100)

for i in range(6):
    forward(180)
    left(60)

left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)

#pen
up()
pensize(10)
color("aqua")
shape(name="circle")
# forward(150)
setposition(0, 50)
down()
color("yellow")
forward("150")



mainloop()