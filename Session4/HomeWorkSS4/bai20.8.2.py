#Bài tập về nhà buổi 6-SS4
#a OUPUT:35
#b OUTPUT: 4
#c OUTPUT: True
#d OUPUT: 0
#e OUPUT: ['apple', 'bananas', 'grapes', 'orange']
#f OUTPUT: False

def add_fruit(inventory, fruit, quantity=0):
    if(fruit not in inventory):
        inventory[fruit] = quantity
    elif(fruit in inventory):
        inventory[fruit] += quantity    
    return inventory
def test(x):
    print(x)
    
# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)