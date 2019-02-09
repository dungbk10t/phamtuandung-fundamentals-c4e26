#Tổng số đo các góc của hình n-giác bằng (n-2).180 độ . 
import turtle
window = turtle.Screen() 

tess = turtle.Turtle() 
tess.pensize(2)

tess.color("blue")
for i in range(3):
    tess.forward(80)
    tess.left(120)

tess.color("red")
for i in range(4):
    tess.forward(80)
    tess.left(90)

tess.color("blue")
for i in range(5):
    tess.forward(80)
    tess.left(72)

tess.color("red")
for i in range(6):
    tess.forward(80)
    tess.left(60)

window.mainloop()    


