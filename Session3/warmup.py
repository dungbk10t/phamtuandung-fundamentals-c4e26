#31/1/2019
# yob_string = (input("Your year of birth ?\n"))

# if(yob_string.isdigit()==True):
#     yob = int(yob_string)
#     if(yob < 2019 and yob > 0):
#         age = 2019 - yob
#         print(age)
#     else:
#         print("yob is error !")    
# else:
#     print("You must  enter a number")  

#C1:
# yob_string = (input("Your year of birth ?\n"))

# while(yob_string.isdigit()==False):
#     print("You must enter a number !")
#     yob_string = (input("Enter again: "))
    
# yob = int(yob_string)
# if(yob < 2019 and yob > 0):
#     age = 2019 - yob
#     print(age)
# else:
    # print("Your yob is error !")    
#C2:
while(True):
    yob_string = (input("Your year of birth ?\n"))
    if(yob_string.isdigit()==True):
        yob = int(yob_string) 
        if(1704 < yob < 2009):
            break
        else:
            print("You must provide a number from 1974 to 2009.")    

    else:
        print("You must enter a number, enter again: ")

age = 2019 - yob
print(age)

