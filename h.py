# def name(a,b):
#     return print(f"{a} {b}")
# a, b = "shiv", "singh"
# name(a.upper(), b.upper(), )



# class test:
#     def __init__(self, m_no, s_no):
#         self.maths = m_no
#         self.science = s_no
#         def total(self):
#             return self.maths + self.science    
#             print(f"the total marks is {total(self)}")



# class score:
#     class test:
#         def __init__(self, m_no, s_no):
#             self.maths = m_no
#             self.science = s_no
#             self.m_total = self.maths + self.science

#             def total(self):
#                 return self.maths + self.science    
#                 # print(f"the total marks is {total(self)}")

#     class attendace:
#         def __init__(self, att):
#             self.attendance = att
#         def att_score(self):
#             return self.attendence/2
#             # print(f"the attendance score is {self.attendance/2}")
    
#     def __init__(self,test, attendance):
#         self.test = test
#         self.attendance = attendance

#         def total(self):
#             test_score = self.test.m_total()/2
#             att_score = self.attendance.att_score()/2
#             return test_score + att_score
#             print(f"the total score is {test_score + att_score}")
# aman_marks = score.test(90, 80)
# aman_att = score.attendace(90)
# aman = score(aman_marks, aman_att).total()
# print(aman)



# class Score:
#     class Test:
#         def __init__(self, maths, science):
#             self.maths = maths
#             self.science = science
        
#         def total(self):
#             return self.maths + self.science

#     class Attendance:
#         def __init__(self, att):
#             self.attendance = att
        
#         def att_score(self):
#             return self.attendance / 2

#     def __init__(self, test, attendance):
#         self.test = test
#         self.attendance = attendance
    
#     def total(self):
#         # assuming equal 50-50 weightage for marks & attendance
#         test_score = self.test.total() / 2
#         attendance_score = self.attendance.att_score() / 2
#         return test_score + attendance_score


# # Example usage
# test_obj = Score.Test(40, 45)        # total = 85
# att_obj = Score.Attendance(90)       # attendance = 90%
# score_obj = Score(test_obj, att_obj)

# print("Final Score:", score_obj.total())

class bank:



    class profile:
        def __init__(self, name, accno, ifdc):
            self.name = name
            self.accno = accno
            self.ifdc = ifdc

        def info(self):
            return f"Name: {self.name}\nAccount Number: {self.accno}\nIFDC: {self.ifdc}"


    class account:
        def __init__(self, balance=0):
            self.balance = balance

        def deposite(self, amount):
                self.balance += amount
                return f"Deposited: {self.balance}"
            
        def withdraw(self, amount):
            if amount > self.balance:
                return f"Withdraw: Insufficent balance"
            else:
                self.balance -= amount
                return f"Withdraw: {self.balance}"
                
    def __init__(self, name, accno, ifdc, balance=0):
        self.profile = self.profile(name,accno, ifdc)
        self.account = self.account(balance)

    def info(self):
        return print(f"Name: {self.profile.name} \nAccount Number: {self.profile.accno} \nIFDC: {self.profile.ifdc} \nBalance: {self.account.balance}")
    
# user = bank("shiv", 123456789, "SBIN0001234")
# user.user_acc = bank.account(1000), bank.account().deposite(500), bank.account().withdraw(200)
 
# print(user.info())

user1 = bank("shiv", 123456789, "SBIN0001234", 10000)
user1.info()
print(user1.account.deposite(5000))
print(user1.account.withdraw(20000))
user1.info()