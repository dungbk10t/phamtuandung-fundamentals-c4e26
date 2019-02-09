#2.1
ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Dung and these are my ship sizes ")
print(ship_sizes)
#2.2
max_size = ship_sizes[0]
for i in range(len(ship_sizes)):
    if max_size < ship_sizes[i]:
        max_size = ship_sizes[i]
print("Now my biggest sheep has size %d let's shear it" %(max_size))
#2.3
for i in range(len(ship_sizes)):
    if ship_sizes[i] == max_size:
        ship_sizes[i] = 8
print("After shearing, here is my flock")        
print(ship_sizes)
#2.4
for i in range(len(ship_sizes)):
        ship_sizes[i]+=50
print("One month has passed, now here is my flock")
print(ship_sizes)        
#2.5
ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Dung and here is my flock")
print(ship_sizes)

for i in range(1,4):
        print("MONTH %d : " %(i))
        for i in range(len(ship_sizes)):
                ship_sizes[i]+=50
        print("One month has passed, now here is my flock")
        print(ship_sizes) 
        max_size = ship_sizes[0]
        for i in range(len(ship_sizes)):
                if max_size < ship_sizes[i]:
                        max_size = ship_sizes[i]
        print("Now my biggest sheep has size %d let's shear it" %(max_size))
        for i in range(len(ship_sizes)):
                if ship_sizes[i] == max_size:
                        ship_sizes[i] = 8
        print("After shearing, here is my flock")        
        print(ship_sizes)
#2.6
print("\n===============2.6===============\n")
ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Dung and here is my flock")
print(ship_sizes)
max_size = ship_sizes[0]
for i in range(len(ship_sizes)):
        if max_size < ship_sizes[i]:
                max_size = ship_sizes[i]
print("Now my biggest sheep has size %d let's shear it" %(max_size))
for i in range(len(ship_sizes)):
        if ship_sizes[i] == max_size:
                ship_sizes[i] = 8
print("After shearing, here is my flock")        
print(ship_sizes)
for i in range(1,3):
        print("MONTH %d : " %(i))
        for i in range(len(ship_sizes)):
                ship_sizes[i]+=50
        print("One month has passed, now here is my flock")
        print(ship_sizes) 
        max_size = ship_sizes[0]
        for i in range(len(ship_sizes)):
                if max_size < ship_sizes[i]:
                        max_size = ship_sizes[i]
        print("Now my biggest sheep has size %d let's shear it" %(max_size))
        for i in range(len(ship_sizes)):
                if ship_sizes[i] == max_size:
                        ship_sizes[i] = 8
        print("After shearing, here is my flock")        
        print(ship_sizes)

print("MONTH 3 : ")
for i in range(len(ship_sizes)):
        ship_sizes[i]+=50
print("One month has passed, now here is my flock")
print(ship_sizes) 
total = 0
for i in range(len(ship_sizes)):
        total += ship_sizes[i]
money = total * 2
print("My flock has size in total: %d"%(total))
print("I would get %d * 2$ = %d$"%(total,money))                