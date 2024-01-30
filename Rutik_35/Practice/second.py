# WAP for compare 3 digit.

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if(a>b and a>c):
    print(a," is maximum number.")
elif(b>a and b>c):
    print(b," is maximum number.")
else:
    print(c," is maximum number.")
