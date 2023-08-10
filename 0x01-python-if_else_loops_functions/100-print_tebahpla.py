#!/usr/bin/python3
# 100-print_tebahpla.py

for i in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(i)}{chr(i - ord('a') + ord('A'))}", end="")
