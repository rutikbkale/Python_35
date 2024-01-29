# WAP for sum of natural number using recurssive function.

def sumFun(n):
    if n <=0:
        return 0
    else:
        return sumFun(n)+sumFun(n-1)
    
n= int(input("Enter the number : "))
print("Sumation is : ",sumFun(n))