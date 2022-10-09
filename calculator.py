print('''
CALCULATOR
Add = A
Substract = S
Multiply = M
Divide = D
''')

no1 = int(input("Enter first no. >> "))
no2 = int(input("Enter second no. >> "))
process = input("Enter what you want to process >> ").upper()

if process == "A":
    print("Added : ", no1 + no2)
elif process == "S":
    print("Substract : ", no1 - no2)
elif process == "M":
    print("Multiply : ", no1 * no2)
elif process == "D":
    print("Divide : ", no1 / no2)
else:
    print("Wrong Input Try Again!")
    