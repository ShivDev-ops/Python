class Employee:
    company_name = "apple"              # this variable created is aassociated with class 
    def __init__(self,name):
        self.name = name                #this variable is associated with object/instance
        self.raise_amt = 0.02
    def showinfo(self):
        print(f"the name of the employee is {self.name} in {self.company_name} and the raise amount is {self.raise_amt}" )


obj = Employee("Rohan")
# Employee.showinfo(obj)          # one argument is given but not show when another way
obj.raise_amt = 0.03
obj.showinfo()

obj1 = Employee("Amit")
obj1.company_name = "Apple India"   # instance variable 
obj1.showinfo()
Employee.company_name = "Google"
obj.showinfo()