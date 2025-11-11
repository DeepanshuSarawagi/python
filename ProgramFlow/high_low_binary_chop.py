low = 1
high = 100000
print("Please enter a number between {} and {}: ".format(low, high))
input("Press Enter to continue...")
guesses = 1

while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if the answer ie correct: ".format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 less than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c.")
    guesses += 1

number = 5
multiplier = 8
answer = 0

for _ in range(multiplier):
    answer += number

print(answer)