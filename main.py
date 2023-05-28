# Define a class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started!")

# Create an object of the Car class
my_car = Car("Tesla", "red")

# Accessing object attributes
print(my_car.brand)  # Output: Tesla
print(my_car.color)  # Output: red

# Calling object methods
my_car.start_engine()  # Output: Engine started!