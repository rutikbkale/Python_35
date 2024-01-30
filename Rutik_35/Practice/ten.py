# WAP to print pattern.
x=[2,4,6,8,10,12,14,16,18,20]
for i in range(1,5,1):
    for j in range(1,5,1):
           if(i>=j):
                 print(x[2*i],end=" ")
                  
    print()
