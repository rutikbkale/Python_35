# WAP to implement the class Vehicle.

class Vehicle:
    def  accelerate(self,speed):
        return speed
    
class Car(Vehicle):
    def __init__(self, speed):
        self.speed = speed
        
    def showSpeed(self):
        print("Speed of the car is : ",self.accelerate(self.speed),"km/hr")

s = int(input("Enter the speed : "))
obj = Car(s)
obj.showSpeed()    