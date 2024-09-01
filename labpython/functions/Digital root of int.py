def digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# User input
number = int(input("Enter an integer number: "))

print("Digital Root:", digital_root(number))
