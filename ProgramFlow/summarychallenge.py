print("Please choose your option from the list below")
print("1. Learn Python")
print("2. Learn Java")
print("3. Go Swimming")
print("4. Have dinner")
print("5. Go to bed")
print("6. Exit")

while True:
    choice = int(input())
    if choice == 1:
        print("You chose Learn Python")
    elif choice == 2:
        print("You chose Learn Java")
    elif choice == 3:
        print("You chose Go Swimming")
    elif choice == 4:
        print("You chose Have dinner")
    elif choice == 5:
        print("You chose Go to bed")
    elif choice == 6:
        print("You chose Exit")
        break
    else:
        print("Invalid choice. Please try again.")
