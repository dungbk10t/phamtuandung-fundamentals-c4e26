import turtle
window = turtle.Screen() 

tess = turtle.Turtle() 
tess.color("red")
tess.pensize(2)

tess.right(30)
tess.forward(80) 
tess.left(60)
tess.forward(80) 
tess.left(120)
tess.forward(80) 
tess.left(60)
tess.forward(80)

for i in range(3):
    tess.right(150)
    tess.forward(80)
    tess.left(60)
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(60)
    tess.forward(80)

window.mainloop()