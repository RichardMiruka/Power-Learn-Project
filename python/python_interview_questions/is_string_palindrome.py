def is_palindrome(string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    string = s.replace(" ", "").lower()

    # Check if the string is the same when reversed to determine if it is a palindrome
    return string == string[::-1]

# Example usage
s = "A man, a plan, a canal: Panama"
if is_palindrome(s):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome") # The string is not a palindrome