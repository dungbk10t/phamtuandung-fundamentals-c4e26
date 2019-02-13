inventory = {
    "gold":500,
    "pouch":["flint","twine","gemstone"],
    "backpack":["xylophone","dagger","bedroll","bread loaf"]
}
for (key,value) in inventory.items():
    print(key,value,sep = " : ")
#1 - 2: add key"pocket" and set value to be a list 'seashell', 'strange berry', and 'lint'.
print("\n#1-2.After add key pocket and value\n")
inventory["pocket"]=["seashell", "strange berry","lint"]
for (key,value) in inventory.items():
    print(key,value,sep = " : ")
#3:remove('dagger') from the list of items stored under the 'backpack' key.
print("\n#3.After remove value dagger of key backpack from dict\n")
inventory["backpack"].remove("dagger")
for (key,value) in inventory.items():
    print(key,value,sep = " : ")
#4:Add 50 to the number stored under the 'gold' key.
print("\n#4.After add 50 to the number stored under the 'gold' key.\n")
inventory["gold"] += 50
for (key,value) in inventory.items():
    print(key,value,sep = " : ")


   


