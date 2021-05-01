def recursive_method(n):
    if n == 1:
        print("Recursion completed, I`m the first method.")
    else:
        print("I`m the method no. {} in the recursion".format(n))
        recursive_method(n-1)


recursive_method(5)
