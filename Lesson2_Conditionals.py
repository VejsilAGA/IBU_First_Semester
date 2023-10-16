number = int(input("Input number 1: "))

if number == 1:
    print("1")
elif number == 2:
    print("2")
elif number == 3:
    print("3")
    
comparison1 = int(input("Input comparison numer 1:"))
comparison2 = int(input("Input comparison number 2:"))

if comparison1==comparison2:
    print("Equal", "=")
elif comparison1>comparison2:
    print("Number 1 is greater than number 2")
else:
    print("Number 2 is greater than number 1")