class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
class ElectricalCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def full_desc(self):
        return f"{self.brand} {self.model} {self.battery_size}"



my_tesla = ElectricalCar("Tesla" , "Model S" , "85kWh" )
print(my_tesla.full_desc())

