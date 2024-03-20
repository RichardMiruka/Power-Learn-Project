class Employee : # Class definition
    def __init__(self, name, age, salary,) : # Constructor method to initialize instance variables
        self.name = name
        self.age = age
        self.salary = salary

    def display(self) :
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)
        
# Testing the code
employee1 = Employee("Richard Miruka", 30, 50000)
employee2 = Employee("Jane Mwaura", 25, 60000)

employee1.display()
print("\n")
employee2.display()