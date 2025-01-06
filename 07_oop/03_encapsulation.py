# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# it don't care about the enternal details.


class Car:
    # brand = None
    # model = None
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        self.total_car += 1
    def full_name(self):
        return f"{self.brand} {self.model}"
    

    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petro or disel"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model) # this takes the value from upper parent class.
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"
    

My_tesla = ElectricCar("Tesla","model x", "85 Kwh")

print(My_tesla.get_brand()) # we cannot access

print (My_tesla.fuel_type())
safari = Car ("Tata", "safari")
print(safari.fuel_type())
BYD = ElectricCar("Atto3", "chinese", "104kw")
print(BYD.fuel_type())

Car("Mecredez","S class")
Car("BMW","X 5")


print(Car.total_car)

## __ this is private
## only accessible from class only. we cannot acces from external. 

# polyformisim is also done from input based. number or string.

#How to track the objects
# sometimes it works during memory optimization.
# it creates problem while garbage correction.