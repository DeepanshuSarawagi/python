# age = int(input("How old are you? "))
# #if (age >=16) and (age <=65):
# if 16 <= age <= 65:  # another way of writing the same code
#     print("Have a good day at work")

name = input("Enter your first name: ")
age = int(input("Please enter your age: "))

if 18 < age < 31:
    print(f"Welcome to the holiday, {name}.")
else:
    print("We are sorry! No slots are available. Please come back after some time")
