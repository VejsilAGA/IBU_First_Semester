import math

x1 = int(input("Enter the x1 coordinate: "))
x2 = int(input("Enter the x2 coordinate: "))
y1 = int(input("Enter the y1 coordinate: "))
y2 = int(input("Enter the y2 coordinate: "))

y = y2 - y1
x = x2 - x1

##d = math.sqrt(math.pow(y, 2) + math.pow(x, 2))

d = math.sqrt(math.pow(y2-y1, 2) + math.pow(x2-x1, 2))


print(d)