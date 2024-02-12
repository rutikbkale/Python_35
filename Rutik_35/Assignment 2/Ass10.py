# Create a function that takes a tuple of coordinates{x,y,z} as an input and returns 3 variables x^2,Y^2,Z^2 representing the sequence of respective coordinates.

def fun1(coordinates): 
    x, y, z = coordinates
    return x**2, y**2, z**2

coordinates = (3, 4, 5)
squared_coordinates = fun1(coordinates)
print("Squared coordinates:", squared_coordinates)
