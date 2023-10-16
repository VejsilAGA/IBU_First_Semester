counter = 0
correct_number = 99

while True:
    guess = int(input("Guess a number: "))
    counter += 1
    if guess == correct_number:
        print("That is the correct number+", correct_number, "The number of attempts was: ", counter-1)
        break
    elif guess < correct_number:
        print("Wrong+ The correct number is greater+")
    else:
        print("Wrong+ The correct number is smaller")
        
#flag alternative
        
flag=True      
while flag:
    guess = int(input("Guess a number: "))
    counter += 1
    if guess == correct_number:
        print("That is the correct number+", correct_number, "The number of attempts was: ", counter-1)
        flag=False
    elif guess < correct_number:
        print("Wrong+ The correct number is greater+")
    else:
        print("Wrong+ The correct number is smaller")