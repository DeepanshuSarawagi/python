# In this lesson we are going to learn about while loops in Python.
# Simple while loop.

i = 0
while i < 10:
    print(f"i is now {i}")
    i += 1

available_exit =["east", "west", "south"]
chosen_exit = ""
while chosen_exit not in available_exit:
    chosen_exit = input("Please enter a direction: ")
    if chosen_exit == "quit":
        print("Game over")
        break
else:
    print("Glad that you got out of here")
