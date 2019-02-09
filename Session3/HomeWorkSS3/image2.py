from turtle import*

colors = ["red", "blue", "brown", "yellow", "grey"]
for i in colors:
    color(i)
    begin_fill()
    for _ in range(2):
        fd(50)
        rt(90)
        fd(80)
        rt(90)
    fd(50)
    end_fill()

mainloop()