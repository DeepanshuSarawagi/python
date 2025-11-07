low = 1
high = 1000
print("Please enter a number between {} and {}: ".format(low, high))
input("Press Enter to continue...")
guess = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if the answer ie correct: ".format(guess)).casefold()
    if high_low == "h":
    # Guess higher. The low end of the range becomes 1 less than the guess.
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
    elif high_low == "c":


