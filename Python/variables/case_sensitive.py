num = 5
Num = 55
print(num) # Output: 5
print(Num) # Output: 55


"""
This Python script demonstrates the difference between a case-sensitive and a case-insensitive language. 
In this example, we have two variables named "num" and "Num". The first variable is in lowercase, and the second variable is in uppercase.
When we print the value of the first variable, it prints 5, and when we print the value of the second variable, it prints 55. 
This program demonstrates the difference between a variable name in lowercase and uppercase. 
It shows that Python is a case-sensitive language, and it treats "num" and "Num" as two different variables.
This shows that Python is a case-sensitive language, and it treats "num" and "Num" as two different variables.
"""

# Path: case_sensitive.py
def print_case():
    with open("case_sensitive.py", "r") as file:
        data = file.readlines()
        for line in data:
            print(line)
            
print_case() # Output: The content of the file "case_sensitive.py" will be printed.
             # This includes comments (indicating the output) and the code.
              
# Now let's try to import the file "case_sensitive.py" and print the variable "num" and "Num".
try:
    from case_sensitive import num, Num
    print(num) # Output: 5
    print(Num) # Output: 55
except ImportError:
    print("The file 'case_sensitive.py' could not be imported.") # Output: The file 'case_sensitive.py' could not be imported.
    print("The module 'case_sensitive' does not exist.") # Output: The module 'case_sensitive' does not exist.
    print("The module 'case_sensitive' is not found.")  # Output: The module 'case_sensitive' is not found.
