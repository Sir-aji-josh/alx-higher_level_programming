#!/usr/bin/python3
# 11-pow.py


def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example usage
print(pow(2, 3))  # Output: 8
print(pow(5, 2))  # Output: 25
