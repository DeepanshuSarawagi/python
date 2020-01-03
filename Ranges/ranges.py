"""In this chapter we are going to learn about ranges in Python."""

myList = list(range(10))
print(myList)

"""This will create a list of elements ranging between 0 and 9"""
even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

"""We can also define the start and end value of ranges. In the above example we have used step of 2 which means 
it will skip every consecutive element in the defined range between 0 and 10 for even and 1 to 10 for odd."""
