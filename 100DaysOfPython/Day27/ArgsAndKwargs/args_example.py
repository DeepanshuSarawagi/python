# In this lesson we are going to learn about *args in function
# *args corresponds any number of positional arguments in a function. We need to specify the no of arguments when
# defining a function. Instead, we can just simply define a function with *args
# See below for better understanding

def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(2, 5, 67, 34, 2, 56, 42, 67)  # As you can see here, we can pass as many parameters when calling a function
