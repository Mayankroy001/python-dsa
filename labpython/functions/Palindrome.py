def is_palindrome(s):
    return s == s[::-1]

# User input
string = input("Enter a string: ")

print("Palindrome:", is_palindrome(string))
