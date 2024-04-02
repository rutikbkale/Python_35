# Define a class report with the following specification.

class Report:
    def __init__(self, adNo, name, marks):
        self.adNo =adNo
        self.name =name
        self.marks =marks

    def calTotal(self):
        total=0
        for mark in self.marks:
            total += mark
        return total

    def calAvg(self):
        return self.calTotal()/5
    
    def displayInfo(self):
        print("Student admission no : ",self.adNo)
        print("Student name : ",self.name)
        print("Student total marks : ",self.calTotal())
        print("Student average : ",self.calAvg())

adNo = int(input("Enter adminssion no :"))
name = input("Enter Student name :")
marks=[]

for i in range(5):
    m=int(input(f"Enter marks for {i+1} subject : "))
    marks.append(m)

obj = Report(adNo, name, marks )
obj.displayInfo()