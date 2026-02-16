numbers = (1, 2, 3, 4, 5)
print(numbers)

print(*numbers)  # This will print each number unpacking them

def test_star(*args):
    print(args)             # Inside a function, args is a tuple of all arguments passed
    for x in args:          # Hence, we can iterate over it to unpack the arguments
        print(x)

test_star(0,1,2,3,4,5,)
test_star()