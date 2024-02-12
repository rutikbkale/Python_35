# WAP to check given element is present in tuple or not.

tuple=(23,45,67,89)
n=int(input("Enter the number : "))
for i in tuple:
    if n in tuple:
        print(n," is present in tuple.")
        break
    else:
        print(n, " is not present.")
        break