import sys


def my_range(n: int):
    print("My range starts")
    start = 0
    while start < n:
        print(f"my_range is returning: {start}")
        yield start
        start += 1


_ = input("line 12")
big_range = my_range(5)
# big_range = range(10000)
_ = input("line 16")

print(f"The size of big range is {sys.getsizeof(big_range)} bytes")
print(f" The size of my range is {sys.getsizeof(my_range)} bytes")


big_list = []

for val in big_range:
    big_list.append(val)


print(f"The size of big list is {sys.getsizeof(big_list)} bytes")
print(big_list)
print(big_range)