# WAP using match.

def converter(num):
   a=int(num)
   return a

def sum(a,b):
   return (a+b)

def sub(a,b):
   return (a-b)

def mult(a,b):
   return (a*b)

def div(a,b):
   return (a/b)

x=input("enter a number : ")
y=input("enter a number : ")
x=converter(x)
y=converter(y)

print("Summation : ", sum(x,y))
print("Subtraction : ", sub(x,y))
print("Multiplication : ", mult(x,y))
print("Division : ", div(x,y))


