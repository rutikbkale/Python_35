# WAP to find the factorial of a number.

a = int(input("Enter the number : "))

f=1
for i in range(1,(a+1)):
    f = f*i
print("Factorial of ",a," is ",f)