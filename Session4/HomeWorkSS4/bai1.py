
#ý 1
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
#ý 2:
for i in prices:
    print(i)
    print("prices: ",prices[i])
    print("stock: ",stock[i])
    
#ý 3:
total = 0
for i in prices:
    total+=prices[i]*stock[i]
print("Total = ",total)

