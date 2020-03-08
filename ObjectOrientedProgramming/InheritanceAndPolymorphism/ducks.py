class Duck(object):

    def walk(self):
        print("Waddle, waddle and waddle")

    def swim(self):
        print("Come on in, the water is lovely.")

    def quack(self):
        print("quack quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, however, it's quite chilly this far South.")

    def quack(self):
        print("Are you `avin' a larf? I'm a Penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
