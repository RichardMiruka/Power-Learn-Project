#The Set is an unordered collection of unique items.
# Set is defined by values separated by commas inside braces { }

# An empty set is created using set() function  that returns an empty set.
# Set is mutable. We can add or remove items from it.  
# If you want to create a set of strings, you should use set().

student_id = {1, 2, 3, 4, 5}    # Set of integers
print(type(student_id))          # <class 'set'>
print(student_id)                # {1, 2, 3, 4, 5}

# Set of mixed datatypes
data = {1, 2.5, "Python", (3, 4, 5)}
print(type(data))               # <class 'set'>
print(data)                     # {1, 2.5, 'Python', (3, 4, 5)}

# An empty set is created using set() function
empty_set = set()            # {} is an empty dictionary
print(type(empty_set))        # <class 'set'>
print(empty_set)              # set()

# Set is mutable. We can add or remove items from it. 
# We can add a single element using the add() method and multiple elements using the update() method.

student_id.add(6)             # Adding a single element
print(student_id)              # {1, 2, 3, 4, 5, 6}

student_id.update([7, 8])      # Adding multiple elements
print(student_id)              # {1, 2, 3, 4, 5, 6, 7, 8}

# To check if an item exists in a set, we can use the in keyword. 
# It returns True if the item is present otherwise False.   

if 9 in student_id:           # Checking if 9 is in student_id
    print("Yes")
else:
    print("No")               # No

# We can also check membership with not operator.

if not 9 in student_id:       # Not (9 in student_id)
    print("Yes")              # Yes     
    
# We can remove an item from a set using the remove() method.
# It raises a KeyError if the item is not found.

try:
    student_id.remove(9)       # KeyError: 9
except KeyError as e:         # Output: KeyError: 9
    print(e)                  # 9 is not in set

# We can use pop() method to remove and return an arbitrary element from a set.
# If there are no elements in the set, it raises a KeyError.

try:
    student_id.pop()           # Removing an arbitrary element & returning it
    print(student_id)          # {1, 2, 3, 4, 5, 6, 7}
except KeyError:              # Output: KeyError: 'pop from an empty set'
    print('Empty set')        # Empty set

# We can use discard() method which tries to remove a specified value from a set. 
# Unlike pop(), it doesn’t raise a KeyError if the value is not found.

student_id.discard(9)          # Trying to remove 9 from student_id
print(student_id)              # {1, 2, 3, 4, 5, 6, 7}

# Sets do not have an index like lists or strings.  
# We cannot access items by their index directly. 

try:
    print(student_id[0])       # TypeError: 'set' object is not subscriptable
except TypeError as e:         # Output: TypeError: 'set' object is not subscriptable
    print(e)                   # Cannot be indexed

# However, we can convert sets into lists so that they can be accessed by indices.

students = list(student_id)    # Convert set to list
print(students[0])             #    1

# To find out whether a specific item exists in a set, we can use the in keyword.

if 9 in student_id:            # True if 9 is in student_id
    print("Yes")               # Yes
else:
    print("No")                # No or False    
    # The count() method returns the number of times a given element appears in the set.

print(student_id.count(9))      # 0 - 9 does not exist in student_id
print(student_id.count(1))      # 1 - 1 exists in student_id

# The union operator (|) returns a new set with all elements from both sets.

mathematics = {8, 9, 10}    # Set of integers
english = {1, 2, 3}         # Another set of integers

combined_subjects = mathematics | english
print(combined_subjects)    # {8, 9, 10, 1, 2, 3}

# The intersection operator (&) returns a new set containing common elements between two sets.

print(mathematics & english)  # {} - There are no common elements

# The difference operator (-) returns a new set with elements that are only in one of the sets.

print(mathematics - english)  # {8, 9, 10} - All elements from mathematics that are not in English  are returned
print(mathematics - english)  # {8, 9, 10} - All elements from mathematics that are not in English  are returned

# The symmetric difference operator (^) returns a new set with elements that are in either of the sets, but not both.

print(mathematics ^ english)  # {8, 9, 10, 1, 2, 3} - All elements that are not common in both sets are returned

# We can use the clear() method to remove all elements from a set.

mathematics.clear()          # Remove all elements from mathematics
print(mathematics)           # set() - Empty set

# We can use the len() method to find the number of elements in a set.
print(len(mathematics))       # 0 - Empty set

# The isdisjoint() method returns True if two or more sets have no common elements.  Otherwise it returns False.
# A frozenset is an immutable version of a set. It’s created using the frozenset() function.
frozen_set = frozenset([4,5,6])   # Create a frozenset
print(type(frozen_set))        # <class 'frozenset'>    
print(frozen_set)              # frozenset({4, 5, 6})

# We can use the isdisjoint() method to check if two sets have any common elements.

print(mathematics.isdisjoint(english))   # True - They have no common elements

# We can iterate over a set using loops just like we do with lists.
for subject in mathematics:
    print(subject)            # No output - Empty set

# However, unlike lists, you cannot access individual elements by their index.
# You need to convert the set to a list first. For example:

list_of_mathematics = list(mathematics)  # Convert set to list
print(list_of_mathematics[0])             # Raises an error if the set is empty

# We can use the any() function to check if a set contains any elements.
print(any(mathematics))         # False - Set is empty

# We can use the all() function to check if all elements in a set satisfy some condition.
print(all(letter in english for letter in mathematics))   # False - All letters in mathematics are not in english
print(all(letter in "abcdefghijklmnopqrstuvwxyz" for letter in "python"))  # True - All letters in python are in the alphabet
print(all(letter in "abc" for letter in english))      # True - All letters in english are in abcdefghijklmnopqrstuvwxyz
print(all(letter in english for letter in mathematics))  # False - None of the letters in mathematics are in english
print(all(letter in english for letter in mathematics))  # False - None of the letters in mathematics are in english
print(all(letter in "abcdefghijklmnopqrstuvwxyz" for letter in "python"))  # True - All letters in python are in the alphabet
print(all(element % 2 == 0 for element in mathematics))   # True - All elements in mathematics are even numbers
print(all(x % 2 == 0 for x in mathematics))  # True - All elements in mathematics are even numbers  (even numbers are 4, 6, 8, 10)
print(all(subject % 2 == 0 for subject in mathematics)) # False - All elements in mathematics are not even numbers
print(all(x % 2 == 0 for x in mathematics))      # True - All elements in mathematics are even numbers  (even numbers are 4, 6, 8, 10)
print(all(x % 2 == 0 for x in mathematics)) # True - All elements in mathematics are even numbers  (even numbers are 4, 6, 8, 10)

# We can use the max() function to find the largest element in a set. If the set is empty, it raises a ValueError.
print(max(english))          # 3 - Largest element in english
print(all(letter <= max(english) for letter in english))      # True - All letters in english are less than or equal to the largest element

# We can use the min() function to find the smallest element in a set. If the set is empty, it raises a ValueError.
print(min(english))          # 1 - Smallest element in english

# The sum() and max() functions return None if the set is empty. To avoid this, you can use the default parameter.
# Sets also support mathematical operations such as union (|), intersection (&), and difference (-).

union = mathematics | english      # Mathematics U English
intersection = mathematics & english # Mathematics N English
difference = mathematics - english  # Mathematics - English

print("Union : ", union)                       # Union :  {1, 2, 3, 4, 5, 6, 8, 9, 10}
print("Intersection : ", intersection)         # Intersection :  {1, 2, 3}
print("Difference : ", difference)             # Difference :  {4, 5, 6, 8, 9, 10}

# The ^ operator performs symmetric difference on sets which means it returns a new set containing only elements that are in either of the sets, but not both.
# The symmetric_difference() method returns the elements that are in either of the sets or in both, but not in their intersection.
# The ^ operator represents symmetric difference which returns elements that are in either of the sets or not in both.
# The ^ operator represents symmetric difference which gives elements that are in either of the sets or neither in both.

symmetric_difference = mathematics ^ english  # Mathematics ^ English
print("Symmetric Difference : ", symmetric_difference)   # Symmetric Difference :  {4, 5, 6, 8, 9, 10}

# Checking Membership with "in" keyword
if 5 in mathematics:     # True - 5 is in mathematics
    print("Yes")         # Yes
else:
    print("No")          # No   is in mathematics
    
# Checking Membership with "not in" keyword
if 7 not in mathematics: # True - 7 is not in mathematics
    print("Not In")        # Not In is not in mathematics 
else:
    print("In")             # In is not in mathematics
    



