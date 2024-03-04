# WAP in python to implement class variable and instrance variable.

class Demo:
    n1,n2=0,0  # this is class variables

    def summation(self, a,b ):  # this is instance variable
        self.n1=a
        self.n2=b
        return self.n1+self.n2

obj = Demo()
sum = obj.summation(10,20)
print("Summation is : ",sum)