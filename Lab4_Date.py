day = int(input("Enter the day: "))
month = int(input("Enter the month: "))

if month==12 and day>= 21 or month<=3 and day<=20:
    print("It is winter")
elif month>=3 and day>=20 or month==6 and day<=21:
    print("It is spring")