"""
    In Python, __init__ is a special method used for initializing objects of a class.
    It's called automatically when a new instance of the class is created. Within the __init__ method, 
    you can define the initial state of the object by assigning values to its attributes.
    
    self is a reference to the instance of the class itself.
    It's used to access variables and methods within the class.
    When you create a new instance of a class,
    Python automatically passes the instance itself as the first argument to every method defined within the class,
    including __init__. 
    By convention, this argument is named self, but you can name it differently if you want.
    Using self, you can access and modify the attributes and methods of the instance within the class.

"""

class Employee : # Class definition
    def __init__(self, name, age, salary,) : # Constructor method to initialize instance variables
        self.name = name # Instance variable 'name' holds the value of attribute 'name'
        self.age = age # Instance variable 'age' holds the value of attribute 'age'
        self.salary = salary # Instance variable 'salary' holds the value of attribute 'salary'
        

    def display(self) : # Method to display the value of instance variables
        print("Name: ", self.name) # Print the value of instance variable 'name'
        print("Age: ", self.age) # Print the value of instance variable 'age'
        print("Salary: ", self.salary) # Print the value of instance variable 'salary'
        
# Testing the code
employee1 = Employee("Richard Miruka", 30, 50000)
employee2 = Employee("Jane Mwaura", 25, 60000)

employee1.display()
print("\n")
employee2.display()
