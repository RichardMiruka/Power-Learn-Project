# print all pairs with given sum

list1 = [8, 7,2,5,3,1]    # This is the list of numbers to search through.
n = len(list1)            # This is the length of the list, which is 6 in this case.
k = 10                    # This is the target sum. The code will look for pairs of numbers in list1 whose sum equals 10

for i in range(0, n):     # The outer loop (i) iterates over each element in the array. The index i represents the position where the smallest value in the unsorted portion of the list will be placed.
    for j in range(i + 1, n): # The inner loop (j)compares the current element with the elements that follow it in the array. The index j represents the position where the next smallest value will be placed 
        if list1[i] + list1[j] == k: # Inside the inner loop, the sum of the elements at positions i and j is calculated. If this sum equals k (which is 10), the code prints the pair.
            print(list1[i], list1[j])
