for i in range(1,20):
    print(f"i is now {i}.")

number = "9,223,456,865,207,590,007"
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i])
