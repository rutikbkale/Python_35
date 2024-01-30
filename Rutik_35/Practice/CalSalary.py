# WAP to create a function to calculate the salary.

salary= int(input("Enter the salary : "))

def calSalary(salary):
    stock=2500
    ha=1750
    nSalary = (salary+stock+ha)*12
    return nSalary

print("Package of Employee : ",calSalary(salary))