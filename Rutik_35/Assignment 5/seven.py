# WAP to create a class BankAcount.

class BankAcount:
    totalAmount=0
    def __init__(self, acNo, amount):
        self.acNo = acNo
        self.totalAmount = amount

    def deposit(self, a):
        self.totalAmount += self.a
        return self.totalAmount
    
    def withdrawal(self, a):
        self.totalAmount -= self.a
        return self.totalAmount
    

class SavingAcount(BankAcount):
    def __init__(self, acNo, amount, ch):
        self.acNo = acNo
        self.amount = amount
        self.ch = ch
        self.a=0
    def details(self):
        super().__init__(self.acNo, self.amount)
        match(self.ch):
            case 1:
                self.a = int(input("Enter the deposite amount : "))
                print(f"Your total balance is : {self.deposit(self.a)}")
            case 2:
                self.a = int(input("Enter the withdrawal amount : "))
                print(f"Your total balance is : {self.withdrawal(self.a)}")
            case _:
                print("please enter valid choice.")

acNo = int(input("Enter the Ac No : "))
amount = int(input("Enter initial amount : "))
print("\n 1.Deposit : \n 2.Withdrawal :  \n\n")
ch = int(input("Enter your choice :"))
obj = SavingAcount(acNo, amount, ch)
obj.details()
            

