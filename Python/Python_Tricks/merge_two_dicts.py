# how to merge two dictionaries in Python 

x = {'a': 1 , 'b': 2}
y = {'b': 3 , 'c': 4}

z = {**x, **y}

print (z)
# Output: {'a': 1, 'b': 3, 'c': 4}

# In Python 2.x you could use this:
# z = x.copy()
# z.update(y)
# print z
