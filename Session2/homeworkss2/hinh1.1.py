import turtle
window = turtle.Screen() 

tess = turtle.Turtle() 
tess.color("red")
tess.pensize(2)

tess.right(19)

tess.forward(80) 
tess.left(38)
tess.forward(80) 
tess.left(142)
tess.forward(80) 
tess.left(38)
tess.forward(80)

for i in range(3):
    tess.right(180-52)
    tess.forward(80)
    tess.left(38)
    tess.forward(80)
    tess.left(142)
    tess.forward(80)
    tess.left(38)
    tess.forward(80)

window.mainloop()

