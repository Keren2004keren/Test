# START
# 1
top: int = int(input("Enter a number: "))
for i in range(1, top + 1):
    print(i, end=" ")
print()

# 2
n1: int = int(input("Enter a number: "))
n2: int = int(input("Enter a number: "))
if n1 > n2:
    for i in range(n2, n1 + 1):
        print(i, end=" ")
else:
    for i in range(n1, n2 + 1):
        print(i, end=" ")
print()

# 3
num_even: int = int(input("Enter a number: "))
for i in range(0, num_even + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 4
max_num: int = int(input("Enter a number: "))
den_num: int = int(input("Enter a number: "))
for i in range(max_num + 1):
    if i % den_num == 0:
        print(i, end=" ")

# STOP
