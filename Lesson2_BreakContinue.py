i = 0

while i < 10:
    i += 1
    print(i)
    if i == 5:
        continue ##code is returned to line 3 (while command)
    if i == 8:
        break
    print(i)