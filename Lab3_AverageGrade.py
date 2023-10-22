grade1=float(input("Enter the first grade: "))
grade2=float(input("Enther the second grade: "))
grade3=float(input("Enther the third grade: "))

amountofgrades=3

totalgrade=grade1+grade2+grade3
averagegrade=totalgrade/amountofgrades

if averagegrade>9.5:
    print("The grade is: 10")
elif averagegrade>8.5:
    print("The grade is: 9")
elif averagegrade>7.5:
    print("The grade is 8")
elif averagegrade>6.5:
    print("The grade is: 7")
elif averagegrade>5.5:
    print("The grade is: 6")

print("The average grade is: ", averagegrade)