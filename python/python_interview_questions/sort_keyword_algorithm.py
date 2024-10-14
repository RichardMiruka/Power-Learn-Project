# sort without using sort keyword algorithm
# This code does not use Python's sort() method
# It performs sorting using a simple nested loop approach.
# The algorithm has a time complexity of O(n²), where n is the number of elements in the list.
# The algorithm has a space complexity of O(1).


def keyword_sort(arr):                   # The function keyword_sort takes an input list arr that we want to sort.
    for i in range(len(arr)):            # The outer loop (i) iterates over each element in the array. The index i represents the position where the smallest value in the unsorted portion of the list will be placed
        for j in range(i + 1, len(arr)): # The inner loop (j)compares the current element with the elements that follow it in the array. The index j represents the position where the next smallest value will be placed
            if arr[i] > arr[j]:          # The inner loop starts from i + 1 and compares the element at position i with the elements that come after it (j), looking for any element smaller than the current arr[i].
                arr[i], arr[j] = arr[j], arr[i] # If the element at index i is greater than the element at index j, the two elements are swapped. This moves the smaller element to the left (closer to the front of the array).
    return arr                           # After sorting all elements, the function returns the sorted list.

# Driver code / Main block of code
if __name__ == '__main__':              # This is the standard Python idiom for ensuring that certain code is run only when the script is executed directly, not when it is imported as a module
    arr = [5, 2, 8, 1, 4, 7, 6, 3]      # The list arr is created with the values 5, 2, 8, 1, 4, 7, 6, 3
    print(keyword_sort(arr)) # [1, 2, 3, 4, 5, 6, 7, 8] # The code initializes the list arr with the values [5, 2, 8, 1, 4, 7, 6, 3] and prints the result of calling keyword_sort(arr). After sorting, the result is [1, 2, 3, 4, 5, 6, 7, 8].
