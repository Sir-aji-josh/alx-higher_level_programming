#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit

# Example usage
result = print_last_digit(12345)  # Output: 5
