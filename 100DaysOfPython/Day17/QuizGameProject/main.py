class User:
    """
    Attribute is a variable associated with the object of class
    methods are functions defined in the class
    """
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def print_user_details(self):
        print("Your name is {}, your age is {} and you are an {} professional".format(self.name, self.age, self.work))


deep = User("Deepanshu", 28, "IT")
deep.print_user_details()
