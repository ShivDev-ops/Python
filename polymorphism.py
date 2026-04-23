## Method Overrinding Ruun-time Polymorphism
##this happens when child class provides a specific implementation of a method that is already defined in its parent class the child class overerindes the parent calss  


# class Vehical:
#     def mode(self):
#         print("Road/Water/Air")
# class Car(Vehical):
#     def mode(self):
#         print("Road")
# class Boat(Vehical):
#     def mode(self):
#         print("Water")
# class Aeroplane(Vehical):
#     def mode(self):
#         print("Air")
# # obj = Vehical()
# # obj.mode()

# obj = [Car(),Boat(),Aeroplane()]
# for i in obj:
#     print(i.mode())


## Method Overloading
##This happen when the multiple method in the same class have same name but differnet paramenters

# class calc:
#     def add(self,a,b):
#         print(a+b)

# obj = calc()
# obj.add(2,3,5)


class Mcalc():
    def add(self,a,b):
        print(a+b)
    # def add(self,a,b,c=None):
    #     if c is not None:
    #         print(a+b+c)
    #     else:
    #         print(a+b)
    # def add(self,a,b,c):
    #     print(a+b+c)
obj = Mcalc()
obj.add(2,3)
# obj.add(2,3)

