# String is a sequence of characters represented by either single or double quotes
name = "John"
print(type(name))  # <class 'str'>
print(name)        # John

# Strings are immutable, meaning they cannot be changed after creation.
try:
    name[0] = 'K' # TypeError: 'str' object does not support item assignment
except Exception as e:
    print(e)

# You can concatenate strings using the + operator to create a new string.
full_name = name + " " + "Doe"
print(full_name)   # John Doe

# Use \ to escape special character like \n for newline or \\ for backslash itself. 
greeting = "Hello,\nHow are you?"
print(greeting)    # Hello,
                    # How are you?  

# You can use triple quotes """ to define multiline strings and it will ignore all whitespace characters.
long_string = """This is a very long string that I am writing out here just so that I can show you how to use triple quotes."""
long_string = """This is a very long string that I am going to write out here just so that I can show you how to use triple quotes."""


# You can access individual characters using indexing. The index starts at 0.
first_letter = full_name[0] # J
print(first_letter)         # J

# Slicing allows you to extract part of a string based on indices. It also returns a new string.
second_last_letter = full_name[-2] # e
print(second_last_letter)          # e

# You can get the length of a string using len() function.
length = len(full_name) # 8
print(length)            # 8

# Check if a substring exists in a string using in keyword.
has_j = "J" in full_name     # True
print(has_j)              # True

# Find the position of a substring using find(). If not found, it returns -1.
position = full_name.find("o") # 4
print(position)           # 4

# Count how many times a substring appears in a string using count().
occurrences = full_name.count("a") # 1
print(occurrences)        # 1

# Split a string into multiple substrings using split(). It returns a list of substrings.
words = full_name.split()   # ['John', 'Doe']
print(words)               # ['John', 'Doe']

# Join multiple strings together using join(). It joins them with an empty string by default.
joined = "\n".join(["I", "love", "Python"]) # I\nlove\nPython
print(joined)                # I
                               # love
                               # Python 
                               
# Convert a string to uppercase using upper().
upper_case = full_name.upper() # JOHN DOE 
print(upper_case)              # JOHN DOE

# Convert a string to lowercase using lower().
lower_case = full_name.lower() # john doe 
print(lower_case)              # john doe

# Remove leading and trailing whitespace using strip().
trimmed = "   John Doe   ".strip() # John Doe
print(trimmed)                      # John Doe

# Replace a substring with another substring using replace().
replaced = full_name.replace("John", "Jane") # Jane Doe
print(replaced)                             # Jane Doe

# Check if a string starts with a substring using startswith().
starts_with = full_name.startswith("Jo") # True
print(starts_with)                         # True

# Check if a string ends with a substring using endswith().
ends_with = full_name.endswith("e")    # True
print(ends_with)                          # True

# You can use format() method to format a string. 
# The {} inside the string is replaced by values provided as arguments to format().
formatted = "Hello, {}!".format("World") # Hello, World!
print(formatted)                            # Hello, World!

# You can use f-string to format a string. It is available in Python 3.6 and above.
name = "John"
age = 25
f_string = f"My name is {name} and I am {age} years old." # My name is John and I am 25 years old.
print(f_string)                                       # My name is John and I am 25 years old.

# You can use the + operator to concatenate strings.
concatenated = "Hello" + ", " + "World!" # Hello, World!
print(concatenated)                                  # Hello, World!

# You can use the * operator to repeat a string.
repeated = "*" * 10 # ******************
print(repeated)                                     # ******************

# You can use the in operator to check if a substring exists in a string.
contains = "Hello" in "Hello, World!" # True
print(contains)                                     # True  

