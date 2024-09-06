#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


# Ensure an argument is provides
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is not defined for negative numbers")
        else:
            f = factorial(num)
            print(f)
    except ValueError:
        print("Error: please provide a valid integer.")
else:
    print("Usage: ./factorial.py <non-negative integer>")
