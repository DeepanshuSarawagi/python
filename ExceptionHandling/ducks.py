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


class Mallard(Duck):
    pass


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if type(duck) is Duck:  # this isn't a pythonic way
        # if isinstance(duck, Duck):  # still this isn't pythonic way
        fly_nethod = getattr(duck, 'fly', None)  # getattr(object, 'method', default)
        """the gettatr() method check`s the object`s dictionary to check the attribute we specified."""
        if callable(fly_nethod):
            self.flock.append(duck)

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, however, it's quite chilly this far South.")

    def quack(self):
        print("Are you `avin' a larf? I'm a Penguin")


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
