# print("hello world !!")
class account:
    def __init__(self,acc_name,acc_no,balance,pin):
        self.acc_name = acc_name
        self.balance = balance
        self.acc_no = acc_no
        self.__pin = pin 
    def withdraw(self,amount, pin):
        self.amount = amount
        self.withdrawtaransation = []
        self.withdrawtaransation.append(amount)
        self.inpin = pin
        if self.inpin == self.__pin :

            if self.balance < self.balance:
                print("Insufficent Balance")
            else:
                self.balance -= self.amount
        else:
            print("Invalid Pin")
        return print("Remaiaing amount is ", self.balance)
    def deposite(self,amount):

        self.amount = amount
        self.depositetaransation = []
        self.depositetaransation.append(amount)
        self.amount = amount
        self.balance += self.amount
        return print("Current amount is ", self.balance)

class Pin(account):
    def __init__(self, acc_name, acc_no, balance, pin):
        super().__init__(self)
        self.newpin = int(input("enter previous pin"))
        if self.newpin == self.__pin:
            self.newpin = self.__pin
        else:
            print("invalid pin")
                
         


class Transaction(account):
    def __init__(self,history,deposite,withdraw):
        self.history = history
        self.depositetaransation = deposite
        self.withdrawtaransation = withdraw
        print(f"the withdraw transaction history is {withdraw}/n the deposite transaction history is {deposite} ")

obj1 = account("Shivendra",12356789,5000,123456)
obj1.withdraw(12345,500)




