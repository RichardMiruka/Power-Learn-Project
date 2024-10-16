# a lambda function is a small anonymous function defined using the lambda keyword.
# It can take any number of arguments, but only one expression, and is often used for short, one-line functions.
# It is similar to a regular function in simple operations where defining a full function is unnecessary.


# Example of a lambda function
add = lambda x, y: x + y    # lambda function to add two numbers x and y 

# Calling the lambda function
result = add(5, 10)         # passing 5 and 10 to the lambda function
print(result) # Output: 15