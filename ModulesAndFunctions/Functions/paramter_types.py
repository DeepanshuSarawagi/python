def func(p1, p2, *args, k, **kwargs):
    """
    Prints the provided positional, variadic, keyword, and variadic keyword arguments.

    This function outputs the arguments passed to it, including required positional
    parameters, variable-length positional arguments, a single required keyword-only
    parameter, and variable-length keyword arguments.

    Arguments:
        p1: Required.
            The first positional parameter.
        p2: Required.
            The second positional parameter.
        *args: Optional.
            Any additional positional arguments.
        k: Required.
            A keyword-only parameter.
        **kwargs: Optional.
            Any additional keyword arguments.
    """
    print("positional-or-keyword args:...{}, {}".format(p1, p2))
    print("var-positional args:..........{}".format(args))
    print("keyword args:.................{}".format(k))
    print("var-keyword args:.............{}".format(kwargs))

func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)