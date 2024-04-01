# Define a class student with the following specification members of class student.

class Student:
    def __init__(self, admno, sname, m1, m2, m3):
        self.admno = admno
        self.sname = sname
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def cTotal(self):
        return self.m1+self.m2+self.m3
    
    def showData(self):
        print("Student adm No : ",self.admno)
        print("Student Name : ",self.sname)
        print("Total Marks : ",self.cTotal())

admno = int(input("Enter student adm No : "))
sname = input("Enter student Name : ")
m1 = float(input("Enter marks for English : "))
m2 = float(input("Enter marks for Science : "))
m3 = float(input("Enter marks for Math : "))

obj = Student(admno, sname, m1, m2, m3)
obj.showData()