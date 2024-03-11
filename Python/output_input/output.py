# In Python, we can simply use the print() function to print output.

# print(object= separator= end= file= flush=)

# print with end whitespace

print("Hello", end=" ")

print("My name is Richard Miruka", end=" ")

print("and I am a software developer")

# print without end whitespace (default value)

print("I love coding in Python.")

# \n represents newline character and \t represents tab character.

print("Python\tloves\tme")  # "Python	loves	me"

print("This\nis\na\nnew\nline")  # "This\nis\na\nnew\nline"

print("This\r\ris\ra\rcarriage\rreturn")  # "This\r\ris\ra\rcarriage\rreturn"

# Using + operator for string concatenation.

name = "Richard"
age = 27
country = "Kenya"

print("My name is " + name + ", I am " + str(age) + " years old and I am from " + country)  # "My name is Richard, I am 27 years old and I am from Kenya"