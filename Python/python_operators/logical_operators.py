# Logical operators are used to check whether an expression is True or False.
# They are used in decision-making.

# Logical operators are used to combine conditional statements. 
# If the condition evaluates as True, the logical operator returns True. Otherwise it returns False.

# There are two types of logical operators:
# - AND (&&) : It returns True if both the conditions are True.
#   Example: print(True && True) # Output: True
#           print(False && True) # Output: False

# - OR (||) : It returns True if at least one of the conditions is True.
#   Example: print(True || True) # Output: True
#            print(False || True) # Output: True

print("AND Operator")
x = 10
y = 20
if x > 5 and y < 30:
    print("Both conditions are True")
else:
    print("At least one condition is False")
    
    
a = 5
b = 6
print (a > 2) and (b >=6) # Output: True
print ((a == 4) and (b == 6)) # Output: False

print("OR Operator")
if a <= 2 or b >= 6:
    print("At least one condition is True")
else:
    print("Both conditions are False")
    
print((a + b) % 2 == 0 or (a - b) % 2 == 0) # Output: True

# NOT Operator (!): Inverts the value of the given expression.
# It returns True if the expression inside ! is False. And vice versa.

print("NOT Operator")
if not (a == 5):
    print("The expression is False")
else:
    print("The expression is True")