""" Parent class or Super class
It is the most base and general class.
It is the class that all other classes are derived from.
It is the class that is inherited from by other classes.
It is the class that does not inherit from any other class.
It is the class that does not have any parent class.
It is the class that does not have any derived class.
"""

class Vehicle: # Parent class or Super class

    def __init__(self, make, model, year): # Constructor method to initialize instance variables
        self.make = make # Instance variable 'make' holds the value of attribute 'make
        self.model = model # Instance variable 'model' holds the value of attribute 'model'
        self.year = year # Instance variable 'year' holds the value of attribute 'year'

    def get_info(self): # Method to return the value of instance variables
        return f'{self.year} {self.make} {self.model}' # Return the value of instance variables in a formatted string

class Car(Vehicle): # Child class or Sub class
    def __init__(self, make, model, year, color): # Constructor method to initialize instance variables
        super().__init__(make, model, year) # Call the constructor method of the parent class to initialize instance variables
        self.color = color # Instance variable 'color' holds the value of attribute 'color' which is specific to Car class only

    def get_info(self): # Method to return the value of instance variables including 'color'
        super().get_info() # Call the method of the parent class to return the value of instance variables excluding 'color'
        return f'{self.year} {self.make} {self.model} ({self.color})' # Return the value of instance variables including 'color'

# Testing the classes
my_car = Car("Toyota", "Corolla", 2015, "red") # Create an object of Car class with values for attributes 'make', 'model', 'year', and 'color'
print(f"Car Info:\n\t{my_car.get_info()}") # Print the value returned by the method of Car class to display the value of instance variables including 'color'

your_car = Vehicle("Toyota", "Corolla", 2015) # Create an object of Vehicle class with values for attributes 'make', 'model', and 'year'my_car = Car("Toyota", "Corolla", 2015, "red")
print(f"\nVehicle Info:\n\t{your_car.get_info()}") # Print the value returned by the method of Vehicle class to display the value of instance variablesmy_car = Car("Toyota", "Corolla", 2015, "red")

# Output    : Car Info:
#                    2015 Toyota Corolla (red)
#             Vehicle Info:
#                    2015 Toyota Corolla (green) 
