#!/usr/bin/python3
import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Print the information about the last digit
print("The string Last digit of", number, "is", last_digit, end=" ")

# Check the conditions for the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
