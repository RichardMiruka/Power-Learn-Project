# Often faster than Merge Sort in practice due to less overhead (no need for auxiliary space for merging).
# est for sorting arrays in place.
# Can be inefficient in its worst case, so it's better to implement randomized Quick Sort to avoid worst case scenario.
# Quick Sort has an average-case time complexity of O(n log n) but can degrade to O(n²) in the worst case

# quick sort algorithm in python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # choose the pivot (in this case, the last element)
        pivot = arr[-1]

        # Elements less than the pivot
        left = [x for x in arr if x < pivot]

        # Elements greater than or equal to the pivot
        right = [x for x in arr[:-1] if x >= pivot]
        
        # Recursively sort left and right and return combined result
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10] # Output: [3, 9, 10, 27, 38, 43, 82]
print("original array:", arr)
sorted_arr = quick_sort(arr)
print("sorted array:", sorted_arr)