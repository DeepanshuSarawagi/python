import sys


def my_range(n: int):
    print("My range starts")
    start = 0
    while start < n:
        print(f"my_range is returning: {start}")
        yield start
        start += 1


big_range = my_range(5)
# big_range = range(10000)
_ = input("line 15")

print(next(big_range))

""" the next value will be returned as 1 when the for loop is executed at line 25 which in-turn calls the  my_range 
function. This happens because the first value of my_range is already consumed by the generator function when called 
at line 17. """

print(f"The size of big range is {sys.getsizeof(big_range)} bytes")
print(f" The size of my range is {sys.getsizeof(my_range)} bytes")


big_list = []

_ = input("line 24")
for val in big_range:
    _ = input("line 26- inside loop")
    big_list.append(val)


print(f"The size of big list is {sys.getsizeof(big_list)} bytes")
print(big_list)
print(big_range)