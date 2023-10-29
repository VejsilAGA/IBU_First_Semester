correct_number = 6

a = int(input("Enter your guess: "))

while(a!=correct_number):
    a = int(input("You are not correct, enter again: "))
    if a == correct_number:
        print("You are correct")