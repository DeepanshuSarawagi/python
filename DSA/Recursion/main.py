def recursive_method(n):
    if n == 1:
        print("Recursion completed, I`m the first method.")
    else:
        print("I`m the method no. {} in the recursion".format(n))
        recursive_method(n-1)


recursive_method(5)

"""
Below beautiful example shows how recursion works. Lets say that we have four methods defined. First method calls
the second method, second method calls the third and so on.. When the first method calls the second method, the first
method execution is stopped and saved in the stack memory. Similarly for second and third. Until the execution of
 fourth method completes, all the other three mnethods will stay STACK memory. Once the execution is completed, 
 STACK memory will then execute third, second and first method. This type of execution is called FILO. 
 First in, Last Out."""


def first_method():
    second_method()
    print("I`m the first method.")


def second_method():
    third_method()
    print("I`m the second method.")


def third_method():
    fourth_method()
    print("I`m the third method.")


def fourth_method():
    print("I`m the fourth method.")


first_method()
