from turtle import*
def draw_square(length_h,color_s):
    for i in range(4):
        pencolor(color_s)
        fd(length_h)
        lt(90)
draw_square(100,"red")   
mainloop()   

