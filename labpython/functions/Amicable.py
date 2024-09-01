def sum_of_divisors(n):
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def are_amicable(num1, num2):
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

# User input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Amicable:", are_amicable(num1, num2))
