#!/usr/bin/python3
# 102-magic_calculation.py


def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s  # Return the original string if n is out of bounds
    
    new_str = ""
    for i in range(len(s)):
        if i != n:
            new_str += s[i]
    
    return new_str

# Test cases
original_string = "abcdef"
new_string = remove_char_at(original_string, 2)
print(new_string)  # Output: "abdef"

