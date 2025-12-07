user_input = input("Enter comma separated numbers: ")
user_input = user_input.split(",")
answer = 0
for number in user_input:
    answer += int(number)
print(answer)