# WAP to check for maximum number between 3 numbers.

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

if(a>b and a>c):
    print(a," is maximum number.")
elif(b>a and b>c):
    print(b," is maximum number.")
elif(c>a and c>b):
    print(c," is maximum number.")
else:
    print("All numbers are same.")
