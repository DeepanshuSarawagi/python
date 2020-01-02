"""In this chapter we are going to learn about Iterators in Python. Iterators are nothing but those objects which
can be counted. Meaning, you can traverse through the object. Strings, Lists, Dictionaries, Sets, Tuples are iterable
objects."""

number = "1234567890"
for char in number:
    print(char)

"""What happens behind the scene is that the for statement calls the iter() on the iterable object.
The function returns an iterator object that defines the method __next__() which accesses elements in the container one 
at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to 
terminate."""
"""Please refer to the below code to understand what happens in the background."""
print()

my_iterator = iter(number)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

"""Basically you get the same output when you execute the for loop."""
