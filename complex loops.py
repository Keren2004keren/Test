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
