#Vẽ đường đi xoắn ốc của rùa
from turtle import *
shape("turtle")

speed(10)
#C1:
for i in range(10,1000,10):
    forward(i) 
    left(90)
#C2:
# for i in range(1000):
#     forward(i*5) 
#     left(90)
#C3:
# d = 10
# for i in range(1000):
#      forward(d) 
#      left(90)
#      d+=10
mainloop()