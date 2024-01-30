# WAP to create a function to calculate average of 5 subject display the student details.

rollno = int(input("Enter the roll number : "))
name = input("Enter the name : ")
marks = [67,70,45,89,70]

print("\nStudent Details \n\n")

def calAvg(marks):
    total =0
    for i in marks:
        total += i
    print("Student Total marks : ",total)
    per = (float)(total/5)
    print("Student Percentage : ",per)
    
print("Student name : ",name)
print("Student roll number : ",rollno)
calAvg(marks)
