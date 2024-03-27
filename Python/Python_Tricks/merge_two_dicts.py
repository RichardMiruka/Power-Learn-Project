# how to merge two dictionaries in Python 

x = {'a': 1 , 'b': 2}
y = {'b': 3 , 'c': 4}

z = {**x, **y}

print (z)
# Output: {'a': 1, 'b': 3, 'c': 4}

# The code combines the key-value pairs from dictionaries x and y into a new dictionary z.
# If there are duplicate keys, the values from y will overwrite the values from x.

# In Python 2.x you could use this:
# z = x.copy()
# z.update(y)
# print z
