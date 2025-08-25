def even_fibonacci_sum(limit):
    """
    Calculate the sum of even Fibonacci numbers less than the given limit.
    """
    # Initialize Fibonacci sequence
    a, b = 1, 2
    total_sum = 0

    while b < limit:
        # If current number is even, add to sum
        if b % 2 == 0 :
            total_sum += b
        #generate next fibonacci number
        a, b = b, a+b

    return total_sum

#solve the problem
limit = 4000000
result = even_fibonacci_sum(limit)
print(f"Sum of even Fibonacci numbers less than {limit}: {result}")