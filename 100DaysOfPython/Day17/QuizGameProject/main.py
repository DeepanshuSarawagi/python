class User:
    """
    Attribute is a variable associated with the object of class.
    @attributes:
        self.name
        self.age
        self.work

    methods are functions defined in the class
    Constructor is a method which is also called as initializing an object.
    The way we create a constructor is using def __init__() method

    Attributes are the things the object has and the methods are the things the objects does

    """
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def print_user_details(self):
        print("Your name is {}, your age is {} and you are a {} professional".format(self.name, self.age, self.work))


deep = User("Deepanshu", 28, "IT")
deep.print_user_details()
rajat = User("Rajat", 26, "Business")
rajat.print_user_details()
