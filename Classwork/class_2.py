# self: helps to store the data in the object and access it using "." syntax
# else it won't store the value in the object so every methord in python has self as a 1st parameter
class Car:
    name_of_shop = "Jayesh" #this is the class attribute, this tied to the class and not to object so all object will have the same value for this varible
    wheels = 4
    def __init__(self,brand): #this is the constructor and always has self
        self.brand = brand  #this will be stored in the object and can be assed by the classes other members; in other words self.brand will create a varible call brand in class but it is tied to object not class

mycar = Car("Toyota")   #this will create a object mycar, so now the self is pointing to mycar means self ----> mycar
print(mycar.brand)  #this will print the brand = Toyota, so self ---> mycar, so if we write self.brand = brand in constructor then it is like writing mycar.brand = "toyota"
mycar.brand = "Honda"
print(mycar.brand) #this will change the exiting copy
print(mycar.name_of_shop)

mycar2 = Car("Volvo")
mycar.name_of_shop = "shruti" #this will not change the class attribute, but it will create same varible named "name_of_shop" for the object and change that;
# Car.name_of_shop ----------> "Jayesh" but the object mycar.name_of_shop ----------> "shruti"
print(mycar.name_of_shop)
print(mycar.__class__.name_of_shop) #this shows that the copy of the name_of_shop in class is not affected
print(mycar2.name_of_shop)

Car.name_of_shop = "shru" #this will change the varible in the class and not the copy so all objects value will be changed

print(mycar.name_of_shop)   # obviously this won't change because it has different copy that override the classes copy
print(mycar2.name_of_shop)  # this will change

print(mycar.__dict__)   #this will show all the attributes in the form of dictionary
print(mycar2.__dict__)  #this will only show the brand attribute becase the object don't have any attribute called name_of_shop it is using attribute from Class Car
print(Car.__dict__)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# check if the attribute exist using hasattr
print(hasattr(mycar, "brand"))
print(hasattr(mycar2, "name_of_shop"))  #this is true becasue class has it
print(hasattr(mycar2, "color"))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# add and delete the attribute in the instance
mycar2.color = "red"
print(hasattr(mycar2, "color"))
print(hasattr(mycar,"color"))   #only for the specific instance or objects only
print(mycar2.color)

Car.color = "blue"
print(hasattr(mycar,"color"))
print(mycar2.color)
print(mycar.color)

del mycar2.color
print(hasattr(mycar2, "color"))
print(mycar2.color)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Class methods 
class Car_new:
    wheels = 4
    numb_car = 0
    def __init__(self,brand): 
      self.brand = brand
      Car_new.numb_car += 1 #we can change the class parameter in the __init__ by using the Class name
    #   cls.numb_car += 1 this wont work it only work in class method
    
    # instance method
    def start_engine (self):        # this is attached to class and not to the object, but can only change the instance or object and cannot change class attributes, this is also call instance method used to change the instance attributes 
        print(f"The {self.brand} is started")

    def show_self_wheels(self):
        print(f"number of wheels assigned to class is {self.wheels}")
    
    # class method
    @classmethod    #if not writen this then cls below will be treated as regular variable and not as class
    def show_cls_wheels(cls):
        print(f"number of wheels assigned to class is {cls.wheels}")
        cls.wheels += 1
    
    #static method
    @staticmethod   #it cannot access or change the varibles in both instance and class
    def print_att():
        print("This can only be used to print basic messages and cannot change anything in method or instance or it cannot even access those varibles")
    
mynewcar = Car_new("Honda")
mynewcar.start_engine()
mynewcar.wheels = 6
mynewcar.show_self_wheels() #this will call the wheels assigned to object or instance and any changes made to wheels in this function will change the instance or object copy and dont affect the class copy
mynewcar.show_cls_wheels()  #this will change the class copy and dont affect the copy in instace or the object becasue this the class method and not the instace method
Car_new.print_att()
mynewcar_2 = Car_new("BMW")
print(mynewcar_2.wheels)    #here will be the class attribute which is updated previously
print(f"this is number of {mynewcar_2.numb_car}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fuction with default value

class Car_default:
    def __init__(self, brand="unknown", color= "white"):
        self.brand = brand
        self.color = color

d_mycar = Car_default()
print(f"{d_mycar.brand}_______{d_mycar.color}")
