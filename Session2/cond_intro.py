# #Conditional statement - các câu lệnh điều kiện

# yob = int(input("Your year of birrth?"))
# age = 2019 - yob
# print(age)
# if age < 10: 
#     print("baby")
# elif age < 18:
#     print("Teenager")
# else: 
#     print("adult")  

# #Bài 1:Nhập vào 1 số kiểm tra số đó  > 13

# n = int(input("Enter a number ?"))
# if n > 13:
#     print(n,'> 13')
# else :
#     print(n,'<= 13')    

# #Bài 2: Nhập vào 1 số kiểm tra số đó  = 13
# n = int(input("Enter a number ?"))
# if n == 13:
#     print(n,'= 13')
# else :
#     print(n,'not equals 13')  

# #Bài 3:
# from random import randint
# print(randint(0, 1000))

# #Bài 4:
# from random import randint #gọi hàm randint trong thư viện import. Hàm randint là hàm sinh sô ngẫu nhiên
# #trong khoảng a,b. randint(a,b)
# claudy = '''                _                                  
#               (`  ).                   _           
#              (     ).              .:(`  )`.       
# )           _(       '`.          :(   .    )      
#         .=(`(      .   )     .--  `.  (    ) )      
#        ((    (..__.:'-'   .+(   )   ` _`  ) )                 
# `.     `(       ) )       (   .  )     (   )  ._   
#   )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
# )  )  ( )       --'       `- __.'         :(      )) 
# .-'  (_.'          .')                    `(    )  ))
#                   (_  )                     ` __.:'          
                                        
# --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.'''
# n = randint(0, 100)
# if n < 30: 
#     print("ranny")
# elif n < 60:
#     print(claudy)
# elif n < 100:
#     print("sunny")
# #key search texttart claudy	

# #Bài 5: Kiểm tra số nguyên tố
# n = int(input("Enter a number ?")) 
# if n < 2: 
#     print(n,"khong phai so nguyen to")
# elif n == 2:
#     print(n,"la so nguyen to")
# elif n % 2 == 0:
#     print(n,"khong phai so nguyen to")
# for i in range(3,n-1,2):
#     if n % i == 0:
#         print(n,"khong la so nguyen to")

# else:
#     print(n,"la so nguyen to")               

# #Bài 6: Kiểm tra 1 số có phải số chẵn:
# n = int(input("Enter a number ?")) 
# if (n % 2) == 0:
#     print(n," la so chan")
# else:
#     print(n," khong phai so chan")  

#Bài 7: User name and password:
from getpass import getpass

print("Well come to Facebook !")
username = input("Enter username: ")
if(username == "C4E"):
    password = getpass("Enter password: ")
    if(password == "celerbrate"):
        print("Facebook is logined !")
    else: 
        print("Password is incorrect !")    
else: 
    print("Login error !")  


