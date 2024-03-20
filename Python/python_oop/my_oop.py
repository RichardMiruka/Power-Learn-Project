class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f'{self.year} {self.make} {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def get_info(self):
        return f'{self.year} {self.make} {self.model} ({self.color})'

# Testing the classes
my_car = Car("Toyota", "Corolla", 2015, "red")
print(f"Car Info:\n\t{my_car.get_info()}")

your_car = Vehicle("Toyota", "Corolla", 2015)
print(f"\nVehicle Info:\n\t{your_car.get_info()}")

# Output    : Car Info:
#                    2015 Toyota Corolla (red)
#             Vehicle Info:
#                    2015 Toyota Corolla (green) 2015 Toyota Corolla
