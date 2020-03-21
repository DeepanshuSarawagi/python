import sys

big_range = range(10000)

print(f"The size of big range is {sys.getsizeof(big_range)} bytes")

big_list = []

for val in big_range:
    big_list.append(val)


print(f"The size of big list is {sys.getsizeof(big_list)} bytes")
