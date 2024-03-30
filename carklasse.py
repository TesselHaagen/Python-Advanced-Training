class Car():
    """
    The classes car, with make, type. color and mileage.
    """
    def __init__(self, make, type, color):
        self.make = make
        self.type = type
        self.color = color
        self.mileage = 0
    
    def info(self):
        """
        Returns the information about the car
        """
        return f"This car has the color {self.color}"
    
    def drive(self, kms):
        """
        Increases the mileage with the driven kms
        """
        self.mileage += kms

car1 = Car("x", "y", "green")

print(car1.mileage)
car1.drive(10)
print(car1.mileage)