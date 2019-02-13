# #Buổi 5,11/2/2019
# items = ["Com","Pho","Bun","Mien"]

# items.remove("Bun")

# print(items)

# print(items)
# #Loop 1:
# for i in range(len(items)):
#     print(items[i])

# #Loop 2"forreach đọc trực tiếp ở list
# i = 1
# for food in items:
#     print(i,food,sep = ". ")   
#     i+=1
# #Update
# items[1] = "Pho Bo"
# print(items[1])

# #Loop 3:
# for i,food in enumerate(items,1): #(1 la start)
#     print(i,food,sep = ". ")
# #Bài tập
# #1: in ra các mục chữ hoa
# favorites = ["NEFLIX","REBULL","Dota","LOL","cf","Lien quan","Anime","Manga","football"]
# for i in range(len(favorites)):
#     print(favorites[i].upper())
# #2: In ra them trước chỉ số    
# for i in range(len(favorites)):
#     print(i+1,favorites[i].upper(),sep = ". ")    

# #3: In ra chỉ số = chữ la mã
# roman = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]
# for i in range(len(favorites)):
#     print(roman[i],favorites[i].upper(),sep = ". ")   

# #hàm chồng 2 list lại
# for roman,favorites in zip(roman,favorites):
#     print(roman,favorites,sep = ". ")    

#U,D in LIST(UPDATE, DELETE)
#Bài tập 2: Update list favorite

favorites = ["death note","nexfix","teaching"]
# print("**" * 25)
# for i in range(len(favorites)):
#     print(i+1,favorites[i],sep = ". ")
# print("**" * 25)

# n = int(input("Position you want to update?"))
# favorites[n-1] = input("Your replacing favorite?")
# print("**" * 25)
# for i in range(len(favorites)):
#     print(i+1,favorites[i],sep = ". ")
# print("**" * 25)
        
#Bài tập 3:
# favorites = ["death note","nexfix","teaching"]
# print("**" * 25)
# for i in range(len(favorites)):
#     print(i+1,favorites[i],sep = ". ")
# print("**" * 25)
# #3.1
# n = int(input("Your position you want to delete?")) - 1
# favorites.pop(n)
# print("**" * 25)
# for i in range(len(favorites)):
#     print(i+1,favorites[i],sep = ". ")
# print("**" * 25)
# #3.2
# q = input("Noi dung you want to delete? ")
# favorites.remove(q)
# print("**" * 25)
# for i in range(len(favorites)):
#     print(i+1,favorites[i],sep = ". ")
# print("**" * 25)
#3.3
loop_count = 0 
while(True):
    choice = int(input("Enter your choice? (1 or 2) ?"))
    if(choice==1):
        n = int(input("Your position you want to delete?")) - 1
        favorites.pop(n)
        for i in range(len(favorites)):
            print(i+1,favorites[i],sep = ". ")
        print("**" * 25)
    elif(choice==2):
        q = input("Noi dung you want to delete? ")
        favorites.remove(q)
        print("**" * 25)
        for i in range(len(favorites)):
            print(i+1,favorites[i],sep = ". ")
        print("**" * 25)   
    else:
        print("Your choice not correct !,PLEASE AGAIN !")   
        n1 = int(input("Enter your choice? (1 or 2) ?"))     
    loop_count+=1
    if(loop_count==3):
        break



