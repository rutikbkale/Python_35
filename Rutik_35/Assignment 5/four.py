# Define a class Aeroplane .

class Aeroplane:
    def __init__(self, fNo, destination, distance):
        self.fNo = fNo
        self.destination = destination
        self.distance = distance

    def calFuel(self):
        if(self.distance<=1000):
            return 500
        elif(self.distance>1000 and self.distance<= 2000):
            return 1000
        else:
            return 2000
        
    def showInfo(self):
        print("Flight No is : ", self.fNo)
        print("Destination is : ", self.destination)
        print("Distance is : ", self.distance,"km")
        print("Fuel required : ", self.calFuel(),"Ltr")

fNo = int(input("Enter the flight no : "))
destination = input("Enter the destination : ")
distance = int(input("Enter the distance in km : "))

obj = Aeroplane(fNo, destination, distance)
obj.showInfo()