languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']

# you can use the `for` loop to iterate over all the elements in a list. 
# In this case, we are going to print each element in the list.

print("Here is a list of programming languages:")

for language in languages:
    print(language) # Python, Java, C++, Ruby, JavaScript will be printed on separate lines
    
# You can also use the `for` loop to iterate over all the elements in a list and print the index of each element.
# You can also use the `len()` function to get the length of the list and use the `range()` function to generate a list of numbers from 0 to the length of the list.

print("Here is a list of programming languages with their index:")

index = 0 # We initialize an index variable to 0

for language in languages:
    print(index, language)
    index += 1 # We increment the index variable by 1 after printing each item.
    
# You can also use the `enumerate()` function to get the index and the element at the same time.
print("Here is a list of programming languages with their index using the `enumerate()` function:")

for index_number, language in enumerate (languages):
    print(index_number, language)
    
# You can also use the `for` loop to iterate over all the elements in a list and print the index of each element in reverse order.
"""The `enumerate()` function adds an index to each element in the list. 
It returns an enumerate object that contains tuples containing the index and the element. """
print("Here is a list of programming languages with their index in reverse order using the `enumerate()` function:")
for index_number, language in enumerate (reversed(languages)):
    print(index_number, language)

# You can also use the `for` loop to iterate over all the elements in a list and print the index of each element in reverse order.
print("Here is a list of programming languages with their index in reverse order:")

# The `list()` function converts the enumerate object to a list.
reverse_programming_languages = list(reversed(languages))

for index_number, language in enumerate (reverse_programming_languages):
    print(index_number, language)
    
# You can also use the `for` loop to iterate over all the elements in a list and print the index of each element in reverse order.
"""Note that the `enumerate()` function adds an index to each element in the list. 
So when we convert it back to a list, the index will be in reverse order."""
print("Here is a list of programming languages with their index in reverse order using the `enumerate()` function:")