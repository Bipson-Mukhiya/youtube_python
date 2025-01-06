#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    # brand = None
    # model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) # this takes the value from upper parent class.
        self.battery_size = battery_size
    

My_tesla = ElectricCar("Tesla","model x", "85 Kwh")
print(My_tesla.model)
print(My_tesla.full_name())
