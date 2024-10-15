# Randomized Quick Sort Algorithm in Python

import random

def partition(arr, low,high):
    # choose a random pivot index between low and high
    pivot_index = random.randint(low,high)
    #move the pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # now proceed with standard partitioning logic
    pivot = arr[high]
    i = low -1 # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            #swap the pivot element to its sorted position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def randomized_quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        # recursively sort elements before partition and after partition
        randomized_quick_sort(arr, low, pi-1)
        randomized_quick_sort(arr, pi+1, high)
    return arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("original array:", arr)
sorted_arr = randomized_quick_sort(arr, 0, len(arr) - 1)
print("sorted array:", sorted_arr) # output [3, 9, 10, 27, 38, 43, 82]

