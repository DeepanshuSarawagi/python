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

for i in range(1, 101):
    print(fizz_buzz_game(i))