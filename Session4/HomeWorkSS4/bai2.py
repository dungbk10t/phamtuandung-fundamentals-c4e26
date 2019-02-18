import random
ran = random.randrange(9,20)
count_loop = 0
answer ={
    "1":4*(ran+3)-9,
    "2":4*(ran+3)-8,
    "3":4*(ran+3)-4,
    "4":4*(ran+3),
}
while(count_loop <= 3):
    print("If x = %d then what is the value of 4(x+3) ?"%(ran))
    for k,v in answer.items():
       print(k,v,sep=". ")
    choice = int(input("Your choice ? ")) 
    if(1<=choice<=4):
        count_loop+=1
        if(choice==4):
            print("Bingo !")
            break
        if(choice==1 or choice==2 or choice==3):
            print(":(")
    else:
        print("Your choice is error, input again !")
        count_loop+=1


 
