import time
t1 = time.process_time()

counter = 0

n1 = int(input("number 1: "))
time.sleep(1)
n2 = int(input("number 2 : "))

for i in range(n1, n2):
    counter += 1

t0 = time.process_time()

print("Elapsed time:", t0, t1)  
   
print("Elapsed time during the whole program in seconds:", t0-t1)