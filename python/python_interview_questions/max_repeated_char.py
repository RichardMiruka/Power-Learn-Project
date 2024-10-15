# Q : Find the maximum repeated character in a string with a time complexity of O(n²)

# we can use a brute-force approach
# In this method, we iterate over each character in the string and, for each character, 
# we count how many times it appears by iterating over the rest of the string.
# This approach will give us a time complexity of O(n²).

def max_repeated_char(s):
    max_count = 0 # To store the maximum count
    max_char = '' # To store the character with maximum count

    # count how many times the current character appears in the string
    for i in range(len(s)):
        current_char = s[i]   # We loop through each character in the string (s[i])
        count = 0

        # count how many times the current character appears in the rest of the string
        for j in range(i+1, len(s)):
            if s[j] == current_char: # if the current character appears in the rest of the string
                count += 1

        # update the maximum count and character if the current count is greater
        if count > max_count:
            max_count = count         # We keep track of the character that appears the most (max_char) and its count (max_count).
            max_char = current_char

    return max_char, max_count


# Driver code
s = "geeksforgeeks"
char, count = max_repeated_char(s)
print(f"The maximum repeated character is {char} with a count of {count}." ) # Output: The maximum repeated character is g with a count of 3. (char, count)
