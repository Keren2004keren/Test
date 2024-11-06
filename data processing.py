# START
# 1
sum_num: int = None
while True:
    num: int = int(input("Enter a number: "))
    if num == -99:
        print(sum_num)
        break
    if sum_num is None:
        sum_num = num
    else:
        sum_num += num

# 2
highest_value: int = None
lowest_value: int = None
while True:
    value: int = int(input("Enter a number: "))
    if value == -99:
        print(None)
        break
    elif value <= 0:
        break
    if highest_value is None or value > highest_value:
        highest_value = value
    if lowest_value is None or value < lowest_value:
        lowest_value = value
if highest_value is not None and lowest_value is not None:
    print(f"The highest value that was entered is {highest_value}.")
    print(f"The lowest value that was entered is {lowest_value}.")

# 3
highest_number: int = None
index_num: int = 0
for i in range(5):
    number: int = int(input("Enter a number: "))
    if highest_number is None or number > highest_number:
        highest_number = number
        index_num += 1
print(f"The highest number that was entered is {highest_number} and it's position is {index_num}. ")

# 4
mul1: int = int(input("Enter a number: "))
mul2: int = int(input("Enter a number: "))
counter: int = 0
if mul2 > 0:
    for _ in range(mul2):
        counter += mul1
elif mul2 < 0:
    for _ in range(mul2):
        counter -= mul1
print(f"The multiplication of {mul1} * {mul2} is {counter}. ")

# 5
num1: float = float(input("Enter a number: "))
hezka1: int = int(input("Enter a number: "))
counter: float = 1
if hezka1 > 0:
    for _ in range(hezka1):
        counter *= num1
elif hezka1 < 0:
    for _ in range(-hezka1):
        counter *= num1
    counter: float = 1 / counter

print(f"The result of {num1}^{hezka1} using multiplication is {counter}.")

# 6
num_digit: int = int(input("Enter a 3 digit number: "))
digit_num: int = int(input("Enter a digit: "))
if 100 <= num_digit <= 999:
    first_digit: int = num_digit // 100
    second_digit: int = (num_digit % 100) // 10
    third_digit: int = num_digit % 10
    if digit_num == first_digit or digit_num == second_digit or digit_num == third_digit:
        print("True")
    else:
        print("False")
else:
    print("The number is not a 3 digit number.")

# 7

# 8
prime_num: int = int(input("Enter a number: "))
for num_prime in range(2, prime_num + 1):
    is_prime: bool = True
    for i in range(2, int(prime_num ** 0.5) + 1):
        if num_prime % i == 0:
            is_prime: bool = False
    if is_prime:
        print(num_prime, end=" ")
