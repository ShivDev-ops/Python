class Khamba:
    class student:
        def __init__(self, stu_name, stu_blance ):
            self.stu_name = stu_name
            self.stu_blance = stu_blance

    def withdraw(self, amount):
            if amount > self.stu_balance:
                return f"Withdraw: Insufficent balance"
            else:
                self.stu_blance -= amount
                return f"Withdraw: {self.stu_blance}"





    def __init__(self, brand, place):
        self.brand = brand
        self.place = place



    
