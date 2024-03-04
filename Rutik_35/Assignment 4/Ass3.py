# WAP in python to implement single inheritance with vehicle and car class.

class Vehicle:

    def ingine(self):
        print("This is ingine of any vehicle.")

class Car(Vehicle):

    color,speed="",0

    def __init__(self, color, speed):
        self.color=color
        self.speed=speed

    def displaySpecification(self):
        super().ingine()
        print("color of car is : ",self.color)
        print("top most speed of car is :",self.speed,"km/hr")

obj = Car("red", 200)
obj.displaySpecification()
