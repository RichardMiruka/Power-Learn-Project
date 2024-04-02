# using namedtuple is way shorter than
# defining a class manually

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')  # create the Car class with color and mileage attributes

my_car = Car(color='red', mileage=3812.4)   # create an instance of the Car class
print(f'The car has {my_car.color} color and {my_car.mileage} mileage')  # The car has red color and 3812.4 mileage
print(f'The car has {my_car[0]} color and {my_car[1]} mileage')  # The car has red color and 3812.4 mileage

# You can also access the fields by index, not just by name:
print(f"The car's color is {my_car.color} and mileage is {my_car.mileage}")  # The car's color is red and mileage is 3812.4
print(f"The car's color is {my_car[0]} and mileage is {my_car[1]}")  # The car's color is red and mileage is 3812.4
print(f"The car's color is {my_car.color} and mileage is {my_car.mileage}")  # The car's color is red and mileage is 3812.4