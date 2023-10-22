a=int(input("Unesite prvi broj: "))
b=int(input("Unesite drugi broj: "))

counter=0

for i in range(a,b,1):
    if i%2 == 0:
        counter+=1

print(counter)