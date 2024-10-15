# Merge sort algorithm in python

def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point of the array
        mid = len(arr) // 2

        # Divide the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call merge_sort on the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two halves
        i = j = k = 0

        # copy data to temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("original array:", arr)
merge_sort(arr)
print("sorted array:", arr) # Output: [3, 9, 10, 27, 38, 43, 82] # The code initializes the list arr with the values [38, 27, 43, 3, 9, 82, 10] and prints the result of calling merge_sort(arr). After sorting, the result is [3, 9, 10, 27, 38, 43, 82]. The merge_sort function sorts the input list arr using the merge sort algorithm. It recursively divides the list into two halves, sorts each half, and then merges the sorted halves back together. The merge operation combines two sorted lists into a single sorted list. The time complexity of merge sort is O(n log n) in the average and worst cases.