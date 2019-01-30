# for i in range(4):
#     print("Dung")
# for i in [0,1,2,3,99,"lala"]:
#     print(i)
# n = int(input("Enter a number: "))
# for i in range(n):
#     # print(i, end="\n") #mặc định nhảy dòng
#     print(i, end=" ") # 2 từ cách nhau 1 dấu cách

#BT1
n1 = int(input("Enter a number: "))
for i in range(n1):
    print(i,end=" ")
#BT2
#C1:
n2 = int(input("Enter a number: "))
for i in range(n2):
    if(i%2==0):
         print(i,end=" ")
#BT3:
Tong = 0
n3 = int(input("Enter a number: "))
for i in range(n3):
    Tong += i
print(Tong)    
#BT2 C2
# n2 = int(input("Enter a number: "))
# r2 = range(0,n2,2)
# print(*r2)

