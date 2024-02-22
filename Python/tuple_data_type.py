# A tuple is an ordered sequence of items same as a list.
# The only difference is that tuples are immutable. 
# Tuples once created cannot be modified. 
# Tuples are used to write-protect data and are
# usually faster than lists as they cannot change dynamically.
#Tuples are enclosed in parentheses ( ) and elements are separated by commas.

#creating a Tuple

product = ('Mobile', 1000, 'Samsung', 'Android') # Tuple of strings and integers
print(type(product))                            # <class 'tuple'>

#accessing the element of tuple
print("Element at index 2:", product[2])       # Samsung

try:
    product[2] = 'Nokia' # TypeError: 'tuple' object does not support item assignment
except Exception as e:
    print(e)
    
#we can access individual characters also using indexing
print("Character at index 3: ", product[3][0])   # Android

#We can convert a string into a tuple using the builtin function tuple()
s = "Hello"
tup = tuple(s)
print(type(tup), tup)                #<class 'str'> Hello

#We can concatenate two tuples using the + operator to create a new tuple.
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b               # (1, 2, 3, 4, 5, 6)
d = c + (7, 8)          # (1, 2, 3, 4, 5, 6, 7, 8)

# We can count the number of occurrences of an element in a tuple using the count() method.
fruit_list = ['apple','banana','cherry','date','apple']
num_apples = fruit_list.count('apple')        # 2

# We can find out if an element exists within a tuple using the in keyword.
element = 'cherry'
if element in fruit_list:
    print(f"{element} exists in the tuple")
else:
    print(f"{element} does not exist in the tuple")

# We can get the index position of an element in a tuple using the index() method.
index = fruit_list.index('date')              # 4

# We can remove duplicates from a tuple by converting it to a set and back to a tuple.
no_duplicates = list(set(fruit_list))           # ['date', 'apple', 'banana', 'cherry']
unique_fruits = tuple(no_duplicates)             # ('date', 'apple', 'banana', 'cherry')    