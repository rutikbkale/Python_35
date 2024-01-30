# WAP to find the sum of all even numbers in given list.

first =[12,34,56,78,11,33,55,43,67,89,90,39]

result=0

for i in first:
    if(i%2==0):
        result += i
print("Summation of even numbers in list : ",result)