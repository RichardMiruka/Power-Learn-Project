# sort a dictionary by keys

my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

# sort the dictionary by keys using dict comprehension
sorted_dict = {k: v for k, v in sorted(my_dict.items())}

print(sorted_dict) # {'d': 1, 'b': 2, 'a': 5, 'c': 8} # The code initializes the dictionary my_dict with the key-value pairs {'a': 5, 'b': 2, 'c': 8, 'd': 1}. It then sorts the dictionary by keys using a dictionary comprehension and the sorted() function. The result is {'d': 1, 'b': 2, 'a': 5, 'c': 8}.
# The sorted_dict dictionary is created using a dictionary comprehension that iterates over the sorted items of the original dictionary my_dict. The sorted() function is used to sort the items by keys before creating the new dictionary. The resulting dictionary is sorted by keys in ascending order.

# sort a dictionary by values
my_dict = {'a': 4, 'b': 3, 'c': 7, 'd': 2}

# sort the dictionary by values using dict comprehension
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])} # The sorted() function is applied to my_dict.items() with a custom key argument. The key=lambda item: item[1] means that the dictionary is sorted based on the second element of each tuple (i.e., the dictionary values).

print(sorted_dict)