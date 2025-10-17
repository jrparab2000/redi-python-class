class Bank:
    def __init__(self): #constructor of class
        print("A new Bank account created")

bA = Bank()

class Person:
    def __init__(self, name, age, height): #self is the name of the object 
        self.name = str(name)
        self.age = age
        self.height = height
        print(f"a new Person created \nheight: {self.height} \nage:{self.age} \nname: {self.name} \nself {str(self.say_hello())}")
    
    # By default all methods are instance methods
    def defend(self):   # all method must have self as input cannot be empty
        print("called defend methord")

    def empty(self):    # pass is used for empty functions because empty function will cause problem so use pass (just move out of function)
        pass

    @classmethod    # this is for class methods which is for the class and common between all objects
    # used for class attribute manipulation change the class varibles
    def print_class_name(cls):
        print(f"class name: ({cls.__name__})")

    
    @staticmethod   #this is used for static method dont use any self or cls common betn all objects
    def say_hello():
        # this is used for inheritance
        print("Hello! this is called at the start of class")


myPerson = Person("Jayesh", 25, 175)
myPerson.print_class_name()
myPerson1 = Person(100, 25, 175)
print(myPerson1.name)


class Car:
    def __init__(self, color, price):
        self.price = price
        self.__price = price #__price this will make sure that price will not be access by others basically making it private

car1 = Car("Red", 1000)
print(car1.price)
# print(car1.__price) 
# this can't be access becasue this is accessing private varible

# -------------------------------------------------------------------

# this class does nothing
#even this is not empty class it also inherite base class in python library of class and it will have all the functions like __init__ already in it just those are blank methods
class dumb:
    pass

#inheritance 

class vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

# class Car_model:
#     def __init__(self, name, mileage, model, price):
#         self.name = name
#         self.mileage =mileage
#         self.model = model
#         self.price = price

# Dont have to again again use the same things can use vehical class to car class

class Car_model(vehicle):
    def __init__(self, model, price):
        self.model = model
        self.price = price

#this is inheritance like name and milage is already inherited from vehical class

#overiding orignal class 
# if same method name child class can override the current base class methods

class base:
    def start(self):
        print("Starting in BASE class")

class child1(base):
    def start(self):
        print("Straing in CHILD 1 class")

class child2(base):
    def start(self):
        print("Straing in CHILD 2 class")

class child3(base):
    pass

v = [child1(), child2(), child3()]

for i in v:
    i.start()