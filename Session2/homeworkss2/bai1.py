mass = float(input("Enter your mass(kg): "))
height = float(input("Enter your height(cm): "))
BIM = mass / ((height/100)**2)
print("BIM = %f" %BIM)
if(BIM < 16):
    print("Severely underweight.")
elif(BIM < 18.5):
    print("Underweight.")
elif(BIM < 25):
    print("Normal.")
elif(BIM < 30):
    print("Overweight.")   
else:
    print("Obese.")    
