class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


# Now we are going to create a class Fish which will inherit properties from the Animal class and also has it's own
# properties

class Fish(Animal):

    def __init__(self):
        super().__init__()  # Initializing all the attributes in super class
        self.num_eyes = 3  # Here we are changing the field num_eyes to 3

    def swim(self):
        print("I can swin in water")

    def print_eyes(self):
        print(self.num_eyes)
