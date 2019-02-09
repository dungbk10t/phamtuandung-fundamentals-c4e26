items=['T-Shirt', 'Sweater']
choice = '0'
while(True):
    choice = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if(choice == "R" or choice == "r"):
        print("Our items: ",end = " ")
        print(*items,sep = ", ")
        
    elif(choices == "C" or choice == "c"):
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items: ",end = " ")
        print(*items,sep = ", ")
        
    elif(choice == "U" or choice == "u"):
        index = int(input("Update position? "))
        items[index-1] = input("New item ?")
        print("Our items: ",end = " ")
        print(*items,sep = ", ")
        
    elif(choice == "D" or choice == "d"):
        index = int(input("Delete position? "))
        del items[index-1] 
        print("Our items: ",end = " ")
        print(*items,sep = ", ")
        
    else:# elif(not(choise =="C" or choise=="U" or choise=="R" or choise=="D")):
        break
        