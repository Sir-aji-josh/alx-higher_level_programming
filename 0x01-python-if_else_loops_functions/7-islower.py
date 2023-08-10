#!/usr/bin/python3
def islower(c):
    # Check if the character's ASCII code is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')

# Test cases
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('5'))  # False
