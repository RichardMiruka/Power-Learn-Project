# Bubble sort algorithm in python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 2, 8, 1, 4, 7, 6, 3]
print("original array:", arr)
sorted_arr = bubble_sort(arr)
print("sorted array:", sorted_arr) # Output: [1, 2, 3, 4, 5, 6, 7, 8] # The code initializes the list arr with the values [5, 2, 8, 1, 4, 7, 6, 3] and prints the result of calling bubble_sort(arr). After sorting, the result is [1, 2, 3, 4, 5, 6, 7, 8].