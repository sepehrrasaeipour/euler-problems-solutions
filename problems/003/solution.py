def largest_prime_factor(n):
    """
    a function for find the largest prime factor of n
    """
    #start with smallest prime number 
    largest_factor = 1

    #step 1: put 2 for prime factor
    #remove all of 2 factor
    while n % 2 == 0:
        largest_factor = 2  #largest prime factor 
        n = n // 2 #devision to 2 

        #step 2: review all odd numbers
        #now we sure to have a odd numbers

    factor = 3 #start with smallest odd number
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n = n // factor

        factor += 2 #for take next odd number

    if n > 1 :
        largest_factor = n

    return largest_factor
    
problem_num = 600851475143

#call function and print the result
result = largest_prime_factor(problem_num)
print(f"the largest prime fuctor of {problem_num} is {result}")
