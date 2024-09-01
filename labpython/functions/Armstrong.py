def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    
    def helper(n, length):
        if n == 0:
            return 0
        else:
            return (n % 10) ** length + helper(n // 10, length)
    
    return n == helper(n, num_len)

# User input
number = int(input("Enter an integer number: "))

print("Armstrong:", is_armstrong(number))
