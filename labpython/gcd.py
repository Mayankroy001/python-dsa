# Get user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Convert the numbers to integers for GCD calculation
a = int(a)
b = int(b)

# Ensure b is non-negative for the loop to work correctly
if b < 0:
    b = -b

# Euclidean algorithm to find GCD
while b > 0:
    r = a % b
    a = b
    b = r

gcd = a
print("GCD is", gcd)
