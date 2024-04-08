# an empty list called my_list
my_list = []

# appending the elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# removing the last element from my_list
my_list.pop()

# sorting my_list in ascending order
my_list.sort()

# finding and printing the index of the value 30 in my_list
index_30 = my_list.index(30)

# printing the final list and the index of the value 30
print("my_list:", my_list)
print("Index of 30:", index_30)
