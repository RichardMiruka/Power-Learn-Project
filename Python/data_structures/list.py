# In Python, lists are used to store multiple data at once
# a list of three numbers 
numbers = [1, 2, 3]
print(numbers) # [1, 2, 3]

# a list of three strings
strings = ["apple", "banana", "cherry"]
print(strings) # ['apple', 'banana', 'cherry']

# you can add two lists together to make a new list with all the elements from both lists.
combined_lists = numbers + strings
print(combined_lists) # [1, 2, 3, 'apple', 'banana', 'cherry']

# if you try and add a number to a string, you will get an error because Python doesn't know how to do that.
try:
    numbers + 4
except TypeError as e:
    print(e) # can only concatenate list (not "int") to list

# but you can use the `+` operator to add a number to a list!
new_list = numbers + [4]
print(new_list) # [1, 2, 3, 4] -> [1, 2, 3, 4]

# you can also use the `*` operator to repeat a list a certain number of times.
repeated_list = numbers * 3
print(repeated_list) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# you can also use the `*` operator to repeat a string a certain number of times.
repeated_string = "hello " * 3
print(repeated_string) # hello hello hello

# you can use the `in` operator to check if an element is in a list.
print(1 in numbers) # True
print("banana" in strings) # True

# you can use the `not in` operator to check if an element is not in a list.
print(5 not in numbers) # True
print("grape" not in strings) # True

# you can use the `len` function to get the length of a list.
print(len(numbers)) # 3
print(len(strings)) # 3

# you can use the `min` function to get the smallest element in a list.
print(min(numbers)) # 1

# you can use the `max` function to get the largest element in a list.
print(max(numbers)) # 3

# you can use the `sum` function to get the sum of all the elements in a list.
total = sum(numbers)
print(total) # 6

