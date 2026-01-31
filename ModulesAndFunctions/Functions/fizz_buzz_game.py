def fizz_buzz_game(number):
    """
    Play the Fizz Buzz game.
    :param number: Number to play
    :return: `Fizz` if the number is divisible by 3.
              `Buzz` if the number is divisible by 5.
              `Fizz Buzz if the number is divisible by 15.
              If otherwise, the number should be returned.
    """
    if (number % 3 == 0) and (number % 5 == 0):
        return 'fizz buzz'
    elif number % 5 == 0:
        return 'buzz'
    elif number % 3 == 0:
        return 'fizz'
    else:
        return str(number)

input("Play Fizz Buzz game? Press enter to continue...")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print("Computer response is {}: ".format(fizz_buzz_game(next_number)))
    next_number += 1
    correct_answer = fizz_buzz_game(next_number)
    players_answer = input("Your answer: ")
    if players_answer != correct_answer:
        print("You lose. The correct answer was {}".format(correct_answer))
        break
else:
    print("Well done! You reached the {}".format(next_number))