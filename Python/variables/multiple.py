#assigning multiple values to multiple variables

a, b, c = 5, 3.2, "Hello"
print(f"{a} {b} {c}")
# Output: 5 3.2 Hello

#print(a) # Output: 5
#print(b) # Output: 3.2
#print(c) # Output: Hello

# Rearranging the order will give an error because not all variables are assigned a value to a variable
#d, e, f = 10, 6, "World", 5.5 # ValueError: too many values to unpack (expected 3)

# You can use extra parentheses if you want to assign some values to one or more variables and the rest to another variable.
# You can use '*' operator to assign remaining values to one variable.
d, e, *f = 10, 6, "World", 5.5
print(f"{d} {e} {f[0]}")
# Output: 10 6 World

# If there is no '*', and more values than variables, it will raise an error.
g, h = 1, 2, 3, 4, 5 # ValueError: too many values to unpack (expected 2)

# To avoid this error, you can add extra underscore '_'. It won't be used and is just a convention.
_ ,h , _= 1, 2, 3, 4, 5
print(h) # Output: 2    
