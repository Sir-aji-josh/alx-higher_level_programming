#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    print(result)

# Example usage
uppercase("Hello, World!")  # Output: HELLO, WORLD!
