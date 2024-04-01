# Define a class Book with following specification.

class Book:
    def __init__(self, bookNo, bookTitle, price, noCopies):
        self.bookNo = bookNo
        self.bookTitle = bookTitle
        self.price = price
        self.noCopies = noCopies

    def totalCost(self):
        cost = self.price*self.noCopies
        return cost
    
    def displayInfo(self):
        print("Book number : ",self.bookNo)
        print("Book name : ",self.bookTitle)
        print("Price of one copy : ", self.price)
        print("Number of copies you want : ",self.noCopies)
        print(f"Total cost {self.noCopies} is : {self.totalCost()}")

bookNo = int(input("Book no :"))
bookName = input("Book name :")
price = int(input("price :"))
noCopies = int(input("Enter the number of copies you want : "))

obj = Book(bookNo, bookName, price, noCopies)
obj.displayInfo()