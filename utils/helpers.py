import time
from math import sqrt

def timer(func):
    """برای اندازه‌گیری زمان اجرای توابع"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"زمان اجرا: {end_time - start_time:.4f} ثانیه")
        return result
    return wrapper

def is_prime(n):
    """بررسی اول بودن عدد"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True