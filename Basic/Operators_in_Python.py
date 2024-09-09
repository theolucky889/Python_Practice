# Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operators
x = 10
print(x)
x = 10 + 2
print(x)
x += 2
print(x)
x -= 4
print(x)
x /= 4
print(x)
x *= 4
print(x)
x **= 4
print(x)
x //= 4
print(x)

# Comparison Operators
x = 10
y = 6
print(x >= y)
print(x == y)
print(x <= y)
print(x > y)
print(x < y)
print(x != y)

# Logical Operators
x = 10
y = 4
print(x == y and x > y)
print(x == y or x > y)

# Identity Operators
x = ["LuckyTendy", "LT"]
y = ["LuckyTendy", "LT"]
print(x is y)
print(x is not y)

# Membership Operators
x = ["LuckyTendy", "LT"]
y = ["LuckyTendy", "LT"]
print("LT" in y)
print("LT" not in y)

# Bitwise Operators
"""
& AND
| OR
~ NOT
^ XOR
"""
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
x = 0
y = 1
print(x & y)
print(x | y)
print(x ^ y)