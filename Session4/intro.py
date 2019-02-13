#Buổi 5. Thứ 2,11/2/2019
# person = ["H.Duc",24,"Hai PHong",Flase,11,True]

# person = {}
# print(person)
# print(type(person))

#mỗi 1 phần tử là 1 pari chứa cặp key-value
# person = {
#     "name" : "H.Duc",
#     "age" : 24,
#     "address" : "Hai Phong",
#     "status" : False,
# }
# #R
# print(person) #in hết
# print(person["address"]) #in từng pair riêng lẻ.

#Bài tập 1:
vocabu = {
    "ge":"Trò trơi",
    "fb":"facebook - mạng xã hội",
    "lol":"Liên minh huyền thoại",
    "dt2":"DOTA 2",
    "cf":"Game đột kích",
    "ig":"Íinstagram",
    "tr":"twitter",
    "gg":"good game",
}
val = input("Your choose ?") 
if val in vocabu:
    print(vocabu[val])
else:
    print("Not found !")    



