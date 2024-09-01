def hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // hcf(x, y)

# User input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("HCF:", hcf(num1, num2))
print("LCM:", lcm(num1, num2))
