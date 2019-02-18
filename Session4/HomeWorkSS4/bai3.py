import random
ran = random.randrange(9,20)
count_loop = 0
import random
ran = random.randrange(9,20)
count_loop = 0
answer1 ={
    "1":4*(ran+3)-9,
    "2":4*(ran+3)-8,
    "3":4*(ran+3)-4,
    "4":4*(ran+3),
}
answer2 ={
    "1":55,
    "2":65,
    "3":75,
    "4":85,
}
count = 0
total = 0
while(True):
    print("If x = %d then what is the value of 4(x+3) ?"%(ran))
    for k,v in answer1.items():
       print(k,v,sep=". ")
    choice1 = int(input("Your choice ? ")) 
    if(1<=choice1<=4):
        if(choice1==4):
            print("Bingo !")
            count += 1
            total += 1
            break
        else:
            print(":(")
            total += 1
            break
while(True):            
    print("Estimate this answer (extract calculation not needder: ")
    choice2 = int(input("Jack scored these marks in 5 math tests: 49,81,72,66 and 52. What is the mean? \n")) 
    if(1<=choice2<=4):
        if(choice2==2):
            print("Bingo !")
            count += 1
            total += 1
            break
        else:
            print(":(")
            total += 1
            break
print("You correctly answer %d out of %d questions"%(count,total))


