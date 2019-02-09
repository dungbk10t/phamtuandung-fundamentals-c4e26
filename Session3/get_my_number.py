#31/1/2019
import random
x = random.randint(0,100)
count = 0
while(count < 7):
    number_str= input("Enter a number: ")
    count+=1  
    if(number_str.isdigit()==True):
        number = int(number_str)
        if(number == x):
            print("Congratulations !")
            break
        elif(number < x):
            print("%d < x" %(number))
        else:
            print("%d > x" %(number))       
                