# sort without using sort keyword 

list1 = [5, 2, 8, 1, 4, 7, 6, 3]
n = len(list1)
for i in range(0, n):
    for j in range(i + 1, n):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1) # [1, 2, 3, 4, 5, 6, 7, 8] # The code initializes the list arr with the values [5, 2, 8, 1, 4, 7, 6, 3] and prints the result of calling keyword_sort(arr). After sorting, the result is [1, 2, 3, 4, 5, 6, 7, 8].