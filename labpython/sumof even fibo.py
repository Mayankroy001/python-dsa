def sum_even_fibonacci(limit):
  """Calculates the sum of even Fibonacci numbers below a limit."""
  fib_prev, fib_next = 0, 1
  sum_even = 0

  while fib_next < limit:
    if fib_next % 2 == 0:
      sum_even += fib_next
    fib_prev, fib_next = fib_next, fib_prev + fib_next

  return sum_even

limit = int(input("Enter the limit: "))
result = sum_even_fibonacci(limit)
print("Sum of even Fibonacci numbers below", limit, "is:", result)
