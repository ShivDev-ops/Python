# A class is blueprint or template for creating object it defines the properties and method that an object of the class will have 
# Properties are the data or state of an object and method are the action behaviour tha an object can perform 

# One of the feature in OOP in python is encapsulation
# which means that he interal state of an object is hidden and can only be accessed or modified through object's method
# this help to protect the data and prevent it from being modified in unexpected ways 

# Another key feature of OOP in python is inheritence 
# which allows allows new class to be created that the inherit properties and the method of existing data 
# this allows code reuse and make it eaasy for creating new classes that has similar functionality to exsisting classes 

# polymorphism 

class Person:
    name = "harry"
    occupation = "Software Developer"
    network = "10$"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
b = Person()
b.name = "Nakita"
b.occupation = "Data Scientist"
a.info()


#  "SD2"
# print(a.name, a.occupation)
b.info()

# Self parameter is a reference to the current instance of the class and is use to access the variable that belongs to that class
class Details:
    name = "shiv"
    work = "backchodi"
    def decrip(self):
        print(f"the thing {self.name} does is {self.work}")

# assing a variable to the class before calling it bitch
object1 = Details()
object1.decrip()




