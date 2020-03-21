import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


big_range = my_range(10000)
# big_range = range(10000)

print(f"The size of big range is {sys.getsizeof(big_range)} bytes")
print(f" The size of my range is {sys.getsizeof(my_range)} bytes")


big_list = []

for val in big_range:
    big_list.append(val)


print(f"The size of big list is {sys.getsizeof(big_list)} bytes")
