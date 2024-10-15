# Bubble sort algorithm in python

def bubble_sort(arr):                       # This is the function that sorts the list arr in ascending order using the bubble sort algorithm.
    n = len(arr)                            # It calculates the length of the input array arr and stores it in n. This is the length of the list, which is 8 in this case.
    for i in range(n):                      # This outer loop runs n times (from i = 0 to i = n-1).
        for j in range(0, n - i - 1):       # he inner loop runs from j = 0 to n - i - 1. This loop compares adjacent elements in the list and swaps them if they are in the wrong order. Why n - i - 1?: After each pass, the largest element has already moved to the correct position, so there is no need to compare the last i elements
            if arr[j] > arr[j + 1]:         # This checks if the current element arr[j] is greater than the next element arr[j + 1]. If so, they are out of order and need to be swapped.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]      #  This swaps the two elements to put them in the correct order.
    return arr                                               # After the sorting is complete, the function returns the sorted array.

arr = [5, 2, 8, 1, 4, 7, 6, 3]
print("original array:", arr)
sorted_arr = bubble_sort(arr)
print("sorted array:", sorted_arr) # Output: [1, 2, 3, 4, 5, 6, 7, 8] # The code initializes the list arr with the values [5, 2, 8, 1, 4, 7, 6, 3] and prints the result of calling bubble_sort(arr). After sorting, the result is [1, 2, 3, 4, 5, 6, 7, 8].