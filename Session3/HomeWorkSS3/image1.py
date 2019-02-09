from turtle import*
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
n = 3 #số cạnh đa giác
for i in range(len(colors)):
    for j in range(n):
        pencolor(colors[i])
        fd(100)
        lt(360/n) #số đo 1 góc của đa giác n cạnh
    n+= 1
mainloop()
