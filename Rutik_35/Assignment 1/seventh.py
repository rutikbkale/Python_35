# WAP for fibonacci sequence.

n = int(input("Enter the number : "))

a,b=0,1
print(a,b,end=" ")
# print(b,end=" ")
for _ in range(n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    c=0