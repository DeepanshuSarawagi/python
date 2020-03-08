class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeee!! This is fun.")
        elif self.ratio == 1:
            print("This is hard work but I`m flying")
        else:
            print("I think I'll just fly.")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle and waddle")

    def swim(self):
        print("Come on in, the water is lovely.")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, however, it's quite chilly this far South.")

    def quack(self):
        print("Are you `avin' a larf? I'm a Penguin")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()
    # test_duck(percy)
