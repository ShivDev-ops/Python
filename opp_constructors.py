class person:
    def __init__(self):
        print("Hey i m a rand")

    def info(self):
        print(f"all {self.name} does is {self.occ}")

# Creating variabke for the class 
'''a = person()
b = person()
b.name = "Shiv"
b.occ = "Randpana"
a.name = "Rand"
a.occ = "Randpana"

a.info()
b.info()'''
#every time a class is called in a constructor it will automatically run the no of time it is called


# A constructor is a special method in a class and initialize an object of a class 
# There are differnt type of constructor
# Constructor are automatically invoked when an object of a class in created  
# The main function of a constructor is to assign value to the data member of the class 
# It cannot return any value other than None 

class details:
    def __init__(self, n, o):
        self.name = n
        self.occ = o 
    def info(self):
        print(f"out of all the thing {self.name} does is {self.occ}")

a = details("shiv", "backchodi")
b = details("Shivendra", "Randpana")
a.info()
b.info()

# constructor is a special method to in a class and intialise an cons4 