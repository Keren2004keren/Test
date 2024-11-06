# START
# 1
dec1: float = float(input("Enter a decimal number: "))
dec2: float = float(input("Enter a decimal number: "))
if dec1 > dec2:
    print(dec2)
    print(dec2)
    print(dec2)
elif dec2 == dec1:
    print(f"{dec1}, The numbers are equal.")
else:
    print(dec1)
    print(dec1)
    print(dec1)

# 2
n1: int = int(input("Enter a number: "))
n2: int = int(input("Enter a number: "))
average: float = (n1 + n2) // 2
print(average)

# 3
num1: int = int(input("Enter a number: "))
num2: int = int(input("Enter a number: "))
num3: int = int(input("Enter a number: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

# 4
movie_length: int = int(input("Enter a movie length in minutes: "))
hours: int = movie_length // 60
minutes: float = movie_length % 60
print(f"The movie length is {hours} hours and {minutes} minutes long.")

# 5
four_digit1: int = 0
while not 1000 <= four_digit1 <= 9999:
    four_digit1: int = int(input("Enter a four digit number: "))
    print(f"The digit in the right is {four_digit1 % 10}.")

# 6
four_digit2: int = 0
while not 1000 <= four_digit2 <= 9999:
    four_digit2: int = int(input("Enter a four digit number: "))
    print(f"The digit second to right is {(four_digit2 % 100 - four_digit2 % 10) // 10}.")

# 7
two_digit1: int = 0
while not 10 <= two_digit1 <= 99:
    two_digit1: int = int(input("Enter a 2 digit number: "))
    asarot: int = two_digit1 // 10
    ahadot: int = two_digit1 % 10
    print(f"The sum of digits in {two_digit1} is {asarot + ahadot}.")

# 8
two_digit2: int = 0
while not 10 <= two_digit2 <= 99:
    two_digit2: int = int(input("Enter a 2 digit number: "))
    tens: int = two_digit2 // 10
    ones: int = two_digit2 % 10
    print(f"The reversed number is {ones * 10 + tens}. ")

# 9
even_odd: int = int(input("Enter a number: "))
if even_odd % 2 == 0:
    print("even.")
else:
    print("odd.")

# 10
paycheck: int = int(input("How much did you get in your paycheck?: "))
tax: float = 0
if paycheck > 50_000:
    tax += (paycheck - 50_000) * 0.51
    paycheck = 50_000
if paycheck > 35_000:
    tax += (paycheck - 35_000) * 0.45
    paycheck = 35_000
if paycheck > 25_000:
    tax += (paycheck - 25_000) * 0.4
    paycheck = 25_000
if paycheck > 18_000:
    tax += (paycheck - 18_000) * 0.3
    paycheck = 18_000
if paycheck > 12_000:
    tax += (paycheck - 12_000) * 0.2
    paycheck = 12_000
if paycheck > 6_000:
    tax += (paycheck - 6_000) * 0.1
    paycheck = 6_000
else:
    tax += 0
print(f"The tax you need to pay is {tax}.")

# 11
age: int = int(input("Enter your age: "))
height: float = float(input("Enter your height: "))
if age < 8:
    print("you can't go on the rollercoaster.")
elif 8 < age < 18 and height < 1.15:
    print("you can't go on the rollercoaster.")
elif 8 < age < 18 and height >= 1.15:
    print("You can go on the rollercoaster.")
else:
    print("You can go on the rollercoaster.")

# STOP
