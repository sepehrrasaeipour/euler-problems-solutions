# Problem 3 - Largest Prime Factor

## Problem Statement
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

## Solution Approach
I used the trial division algorithm to efficiently find the prime factors of the large number. The algorithm starts by dividing the number by the smallest prime factor (2) and continues with odd numbers until the number becomes 1. The last factor found is the largest prime factor.

## Code
The solution is implemented in Python (`solution.py`).

## Result
The largest prime factor of 600851475143 is **6857**.