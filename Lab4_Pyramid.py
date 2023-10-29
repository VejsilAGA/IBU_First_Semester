num = str(input("Enter a number: "))

for num in range(1,6):
    print(str(num)*num)
    
rows = int(input("Enter number of rows: "))
for num in range(rows, 0, -1):
    for j in range(num):
        print(num, end=" ")
    print("")