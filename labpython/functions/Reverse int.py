def reverse_number(number):
    original_number = number
    reverse = 0
 
    for _ in str(number):
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
 
    print(f"Original Number: {original_number}")
    print(f"Reversed Number: {reverse}")

# User input
number = int(input("Enter an integer number: "))

# Call the function
reverse_number(number)
