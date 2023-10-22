num1=int(input("Please enter the number1: "))
num2=int(input("Please enter the number2: "))

sign=input("Please enter the function, + or - : ")

sabiranje=num1+num2
oduzimanje=num1-num2

if sign =='+':
    print("The addition of the two numbers is: ", sabiranje)
elif sign =='-':
    print("The subtraction of the two numbers is: ", oduzimanje)
else:
    print("Invalid statement")