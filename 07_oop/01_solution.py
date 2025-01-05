

# take the example of banking form.

# make class name capitalize
# self = context  in javascript it is this->
# self is used to connect the wire to call its own variable
# we need to put the connection line. 
# this is used in different format

class Car:
    # brand = None
    # model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
        
my_car = Car("BYD","ATTO 3")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

#till now we have created a blank form.

my_second_car = Car("Tata", "Safari")
print(my_second_car.brand)
print(my_second_car.model)
print(my_second_car.full_name())
