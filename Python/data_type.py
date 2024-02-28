num1 = 5
print(num1, "is of type", type(num1))  # Output: 5 is of type <class 'int'>

num2 = 3.2
print(num2, "is of type", type(num2))  # Output: 3.2 is of type <class 'float'>

num3 = 1 +2j
print(num3, "is of type", type(num3))  # Output: (1+2j) is of type <class 'complex'>

num4 = "Hello"
print(num4, "is of type", type(num4))  # Output: Hello is of type <class 'str'>

num5 = [1,2,3]
print(num5, "is of type", type(num5))  # Output: [1, 2, 3] is of type <class 'list'>

num6 = (1,2,3)
print(num6, "is of type", type(num6))  # Output: (1, 2, 3) is of type <class 'tuple'>

num7 = {1,2,3}
print(num7, "is of type", type(num7))  # Output: {1, 2, 3} is of type <class 'set'>

num8 = {1: 'one', 2: 'two', 3: 'three'}
print(num8, "is of type", type(num8))  # Output: {1: 'one', 2: 'two', 3: 'three'} is of type <class 'dict'>

num9 = range(5)
print(num9, "is of type", type(num9))  # Output: range(0, 5) is of type <class 'range'>



# data type represents a kind of value and determines 
# how the value can be used in expressions and operations.

# A variable (container in a computer memory)is a name that refers to a value. 
# In Python, variables can be assigned different data types.
# Python has the following data types built-in by default, in these categories:

# Numeric Types: int, float, complex
# Text Type: str
# Sequence Types: list, tuple, range
# Mapping Types: dict
# Set Types: set, frozenset
# Boolean Type: bool
#  None Type: None
# Binary Types: bytes, bytearray, memoryview

# You can get the data type of any object by using the type() function:

#concatenation (add) of two strings
result_string = num4 + " " + "World"
print("Concatenated string result: ", result_string)  # Output: Concatenated string result:  Hello World
print("Type of concatenated string result: ", type(result_string))  # Output: Type of concatenated string result:  <class 'str'>
print(type(result_string), "\n")  # Output: <class 'str'>