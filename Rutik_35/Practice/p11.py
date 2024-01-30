# WAP to take number as a input and check wheather it is divisible by 2 and 3 or only 2 or only 3 or none.

n =int (input("Enter the number : "))
if(n%2==0 and n%3==0):
    print(n," is devisible by 2 and 3.")
elif(n%2==0):
    print(n," is devisible by only 2.")
elif(n%3==0):
    print(n," is devisible by only 3.")
else:
    print(n," is not devisible by 2 or 3.")
