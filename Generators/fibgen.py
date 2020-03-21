def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

for i in range(50):
    print(next(fib))


def odd_numbers():
    num = 1
    while True:
        yield num
        num += 2


oddNumbers = odd_numbers()
for i in range(101):
    print(f"i is now {i} and odd number is {next(oddNumbers)}")
