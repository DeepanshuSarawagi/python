"""
In this lesson we are going to learn about Python Type Hints.
We declare the datatype of a variable before initialising it so that will help us to prevent from TypeError.
We can also do this in functions which accepts arguments, to make sure right datatype of arguments are passed in
functions.
"""

age: int
height: float
name: str
is_human: bool

age = 28
height = 177
name = 56  # As you notice we immediately get a type error here since name is of type String and we declared with value
# of type int
is_human = "yes"  # As you notice we immediately get a type error here since is_human is of type boolean and we declared
# with value of type string


def show_basic_info(age: int, name: str, height: float):
    print("My name is {} and I'm {} years old. My height is {} cms. ".format(name, age, height))


show_basic_info(age="Twenty Eight", name=28, height=178.8)  # If you notice, we get a type error here as well


def can_you_drive(age: int) -> bool:  # Here also we are adding a Type Hint which says this function is expected
    # to return data of type boolean
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(can_you_drive(age=28))
