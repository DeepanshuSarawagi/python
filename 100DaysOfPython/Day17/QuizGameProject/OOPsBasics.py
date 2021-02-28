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
        self.followers = 0
        self.following = 0

    def print_user_details(self):
        print("Your name is {}, your age is {} and you are a {} professional. You have {} followers"
              .format(self.name, self.age, self.work, self.followers))

    def follow(self, user):
        user.followers += 1
        self.following += 1


deep = User("Deepanshu", 28, "IT")
rajat = User("Rajat", 26, "Business")
deep.follow(user=rajat)
deep.print_user_details()
rajat.print_user_details()
