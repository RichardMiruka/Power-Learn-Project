# A list is an ordered collection of similar or
# different types of items separated by commas 
# and enclosed within brackets [ ].

languages = ['Python', 'Java', 'C++', 'Ruby', 'C#'] # List of strings
print(languages) # Output: ['Python', 'Java', 'C++', 'Ruby', 'C#']

#Accessing elements of a list
print(languages[0]) # Output: Python (access first element)
print(languages[1]) # Output: Java (access second element)
print(languages[-1]) # Output: C# (access last element)


#Slicing a list returns a new list containing the elements from the specified range.
print(languages[2:4]) # Output: ['C++', 'Ruby'] (access elements from index 2 to 3)
print(languages[:3]) # Output: ['Python', 'Java', 'C++'] (access elements from index 0 to 2)
print(languages[::-1]) # Output: ['C#', 'Ruby', 'C++', 'Java', 'Python'] (reverse the list)

#Lists are mutable, meaning that their size can change over time.
# This is because lists are implemented using arrays,
# which are mutable in most programming languages.  

#Adding elements to a list
languages.append('PHP') # Add at end of the list
print(languages) # Output: ['Python', 'Java', 'C++', 'Ruby', 'C#', 'PHP']

languages.insert(1, 'Perl') # Insert at specific position
print(languages) # Output: ['Python', 'Java', 'Perl', 'C++', 'Ruby', 'C#', 'PHP']

#Removing elements from a list
languages.remove('Java') # Remove the first occurrence of value Java
print(languages) # Output: ['Python', 'Perl', 'C++', 'Ruby', 'C#', 'PHP']

del languages[5] # Delete the sixth element in the list (index starts with 0)
print(languages) # Output: ['Python', 'Perl', 'C++', 'Ruby', 'C#']

empty_list = []
empty_list.clear() # Clear all elements of the list
print(empty_list) # Output: []  (empty list)        