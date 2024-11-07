# Start
# 1
temp_list: list[float] = []
for i in range(12):
    while True:
        try:
            temp: float = float(input("Enter the temp: "))
            if temp == 0:
                if len(temp_list) > 0 and temp_list[-1] == 0:
                    print("Multiple 0, please enter the temp again.")
                    continue
                else:
                    print("correct data.")
                    temp_list.append(temp)
                    break
            elif temp < -5 or temp > 40:
                print("wrong data.")
                break
            else:
                print("correct data.")
                temp_list.append(temp)
                break
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
if len(temp_list) == 12:
    print(f"The average temperature is {sum(temp_list) / len(temp_list)}.")
    print(f"The highest temperature is: {max(temp_list)}.")
    print(f"The lowest temperature is: {min(temp_list)}.")

# 2
print("Each number represents a vote.\n1- In Favor\n2- Against\n3- Avoid\n4- Veto")

vote1: list[int] = []
vote2: list[int] = []
vote3: list[int] = []
countries_count: int = 0
first_vote1: int = None
last_vote2: int = None
for i in range(44):
    while True:
        try:
            vote: int = int(input("Please enter your vote: "))
            if vote not in [1, 2, 3, 4]:
                print("This number is not an option, please try again:")
                continue
            if vote == 4:
                countries_count += 1
                print(f"The {countries_count} country has vetoed this decision.")
                break
            elif vote == 1:
                vote1.append(vote)
                if countries_count == 0:
                    countries_count += 1
                first_vote1 = countries_count
            elif vote == 2:
                vote2.append(vote)
                countries_count += 1
                last_vote2 = countries_count

            else:
                vote3.append(vote)
                countries_count += 1
        except ValueError:
            print("Invalid input, please try again.")
    if vote == 4:
        break
print(f"{len(vote1)} countries voted in favor.")
print(f"{len(vote2)} countries voted against.")
print(f"{len(vote3)} countries avoided making a decision.")
if first_vote1 is not None:
    print(f"The {first_vote1} country was the first one to vote in favor.")
if last_vote2 is not None:
    print(f"The {last_vote2} country was the last country to vote against.")
