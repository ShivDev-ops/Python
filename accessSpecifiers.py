# class Employee:
#     def __init__(self,name):
#         self.name = name
# a = Employee("Rohan")
# print(a.name)

class Employee:
    def __init__(self,name):
        self.__name = name
a = Employee("Rohan")
# print(a.__name)        #it will throw an error because the attribute is private
print(a._Employee__name)   # <object>._<class>__<attribute>