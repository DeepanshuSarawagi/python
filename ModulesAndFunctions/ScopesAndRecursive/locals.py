def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            print(f"locals of spam3 are {locals()}")
            return z

        y = " more spam"
        y += spam3()
        print(f"locals of spam2 are {locals()}")
        return y

    x = "spam "
    x += spam2()
    print(f"locals of spam1 are {locals()}")
    return x


print(spam1())


def spam1():

    def spam2():

        def spam3():
            z = ' even '
            z += y
            print(f"locals of spam3 are {locals()}")
            return z

        y = ' more' + x
        y += spam3()
        print(f"locals of spam2 are {locals()}")
        return y

    x = " spam"
    x += spam2()
    print(f"locals of spam1 are {locals()}")
    return x


print(spam1())
