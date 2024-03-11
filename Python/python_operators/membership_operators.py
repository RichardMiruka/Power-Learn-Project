# In Python, in and not in are the membership operators. 
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set, and dictionary).

# In a dictionary, we can only test for the presence of a key, not the value.

# In a set, we can only test for the presence of an element, not the value.

def is_in(element, container):
    if element in container:
        return True
    else:
        return False

def is_not_in(element, container):
    if element not in container:
        return True
    else:
        return False

my_dict = {'a':1, 'b':2, 'c':3}
print(is_in('a', my_dict)) # Output: True
print(is_not_in('d  ', my_dict)) # Output: True

my_set = {1, 2, 3, 4, 5}
print(is_in(3, my_set)) # Output: True
print(is_not_in(6, my_set)) # Output: True