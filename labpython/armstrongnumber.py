def check_armstrong(num):
    # Single-digit numbers are Armstrong numbers
    if num in range(1, 10):
        return True

    order = len(str(num))
    sum = 0
    original = num

    while num > 0:
        digit = num % 10
        sum += pow(digit, order)
        num = num // 10

    if sum == original:
        return True
    return False

# Take user input
number = int(input("Enter your number: "))

# Check and print if the number is an Armstrong number
if check_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
