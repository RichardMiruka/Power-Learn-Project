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