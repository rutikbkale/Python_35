# Create a class representing a person with attributes name, age and address.

class Person:
    name=""
    age=0
    address=""

    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print("\nPerson information : \n")
        print("Person name : ",self.name)
        print("Person age : ",self.age)
        print("Person address : ",self.address)

n=input("Enter your name : ")
a=int(input("Enter your age : "))
add=input("Enter your address : ")

obj = Person(n,a,add)
obj.display()
