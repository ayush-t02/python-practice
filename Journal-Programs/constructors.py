# 1. Default constructor
class Default:

    # default constructor
    def __init__(self):
        self.name = "default_object"

    # a method for printing data members
    def print_name(self):
        print(self.name)


# creating object of the class
obj = Default()

# calling the instance method using the object obj
obj.print_name()

# 2. Parameterized constructor
class Addition:
    a = 0
    b = 0
    answer = 0

    # parameterized constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("First number = " + str(self.a))
        print("Second number = " + str(self.b))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.a + self.b


obj = Addition(150, 60)

obj.calculate()

# display result
obj.display()
