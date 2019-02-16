# #Buổi 5. Thứ 2,11/2/2019
# person = ["H.Duc",24,"Hai PHong",Flase,11,True]

# person = {}
# print(person)
# print(type(person))

#mỗi 1 phần tử là 1 pari chứa cặp key-value

# #R
# print(person) #in hết
# print(person["address"]) #in từng pair riêng lẻ.

#Bài tập 1:
# vocabu = {
#     "ge":"Trò trơi",
#     "fb":"facebook - mạng xã hội",
#     "lol":"Liên minh huyền thoại",
#     "dt2":"DOTA 2",
#     "cf":"Game đột kích",
#     "ig":"Íinstagram",
#     "tr":"twitter",
#     "gg":"good game",
# }
# val = input("Your choose ?") 
# if val in vocabu:
#     print(vocabu[val])
# else:
#     print("Not found !")    

#Buổi 6:
# person = {
#     "name" : "H.Duc",
#     "age" : 24,
#     "address" : "Hai Phong",
#     "status" : False,
#     "favs":["book","movie","music"],
# }
# fs = person["favs"]

# for fav in person["favs"]:
#     print(fav)
# for fav in fs:
#     print(fav)
# person["friends_count"] = 450
# person["age"] += 2 #updated
# print(*person.values(),set="\n")
# del person["age"]
# for v in person.values():
#     print(v)

#Bài tập
# vocabu = {
#     "ge":"Trò trơi",
#     "fb":"facebook - mạng xã hội",
#     "lol":"Liên minh huyền thoại",
#     "dt2":"DOTA 2",
#     "cf":"Game đột kích",
#     "ig":"Instagram",
#     "tr":"twitter",
#     "gg":"good game",
# }
# while(True):
#     for k in vocabu.keys():
#         print(k,end="   ")
#     your_code = input("\nYour code ? ")
#     if your_code == "exit":
#         break   
#     if your_code not in vocabu:
#         nhap = input("Not found ! Do you want to contribute this word ? (Y/N): ").upper()
#         if(nhap=="Y"):
#             new_key = input("Enter new key: ")
#             new_value = input("Enter new value: ")
#             vocabu[new_key] = new_value
#             print("Updated")
#         else:
#             break    
#     else:
#         break  
     
# p0 = {
#     "name" : "H.Duc",
#     "age" : 24,
#     "address" : "Hai Phong",
#     "status" : False,
# }
# p1 = {
#     "name" : "Hoang",
#     "age" : 21,
#     "address" : "Ha Noi",
#     "status" : "Suyt",
# }
# p2 = {
#     "name" : "Son",
#     "age" : 18,
#     "address" : "Hung Yen",
#     "status" : True,
# }
person_list = [
    {
    "name" : "H.Duc",
    "age" : 24,
    "address" : "Hai Phong",
    "status" : False,
    },
    {
    "name" : "Son",
    "age" : 18,
    "address" : "Hung Yen",
    "status" : True,
    },
    {
    "name" : "Son",
    "age" : 18,
    "address" : "Hung Yen",
    "status" : True,
    },
]
 
# person_list.append(p0)
# person_list.append(p1)
# person_list.append(p2)

# print(person_list[1]["name"])
# print(person_list[1]["status"])
# for p in person_list:
#     print(p["name"],p["age"])
# print(person_list[0]["address"])
     