import time

def timer(func):
    """دکوراتور برای اندازه‌گیری زمان اجرای توابع"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def problem_1_solution(limit=1000):
    """
    پیدا کردن مجموع تمام مضرب‌های ۳ یا ۵ زیر limit
    Find the sum of all multiples of 3 or 5 below the given limit
    """
    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Alternative solution using list comprehension
@timer
def problem_1_solution_v2(limit=1000):
    """
    More optimized solution using list comprehension
    """
    return sum(i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    # Program title
    print("Project Euler - Problem 1 Solution")
    print("=" * 50)

    # Calculate solution with first method
    solution_1 = problem_1_solution(1000)
    print(f"Problem 1 solution (Method 1): {solution_1}")

    # Calculate solution with second method
    solution_2 = problem_1_solution_v2(1000)
    print(f"Problem 1 solution (Method 2): {solution_2}")
    
    # Test with small case to verify correctness
    test_result = problem_1_solution(10)
    print(f"Test with limit=10 (should be 23): {test_result}")
    
    # Verify test correctness
    if test_result == 23:
        print("✅ Test passed successfully")
    else:
        print("❌ Test failed")