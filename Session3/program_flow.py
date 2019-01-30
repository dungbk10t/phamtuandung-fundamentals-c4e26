import turtle
window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Tess & Alex")
alex = turtle.Turtle()

for i in range(4):
    alex.forward(50)
    alex.left(90)

for color in ["yellow", "red", "purple", "blue"]:
    alex.color(color)
    alex.forward(50)
    alex.left(90)
    
alex.penup()
alex.forward(100) # This moves alex, but no line is drawn
alex.pendown()