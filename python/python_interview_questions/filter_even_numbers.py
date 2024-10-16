# Question:
# You're tasked with writing a Python function,
# that takes a list of integers and returns a list of only
# the even numbers. 
#Could you walk me through how you would approach this problem
# and explain the logic behind the code?"

def filter_even_numbers(numbers):
    even_numbers = []                   #  initialize an empty list to store the even numbers
    for number in numbers:              #  loop through each number in the input list
        if number % 2 == 0:             # check if the number is even by dividing it by 2 and checking the remainder     
            even_numbers.append(number) # if the number is even, add it to the list of even numbers
    return even_numbers                 # return the list of even numbers


# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = filter_even_numbers(numbers)
print(result)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]