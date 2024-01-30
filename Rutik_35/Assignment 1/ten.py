# WAP for sum of natural number using recurssive function.

def sumFun(n):
    if n <=0:
        return n
    else:
        return n+sumFun(n-1)
    
n= int(input("Enter the number : "))
print("Sumation is : ",sumFun(n))