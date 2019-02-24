from turtle import*
import ex5
speed(0)
color("blue")
for i in range(100):
    import random
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(3,10)
    ex5.draw_star(x,y,length)