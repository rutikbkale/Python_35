# WAP to print 1 to 100 prime numbers.

print("Prime numbers between 1 to 100")

for i in range(2,101):
    p=True
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
           p=False
           break
    if p:
        print(i,end=" ")
    
