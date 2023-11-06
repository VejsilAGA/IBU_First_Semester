def loneSum(a, b, c):
    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c

# Test cases:
print(loneSum(1, 2, 3))
print(loneSum(3, 2, 3))
print(loneSum(3, 3, 3))