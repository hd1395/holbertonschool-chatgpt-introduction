#!/usr/bin/python3

"""
Factorial Calculator Script

This script calculates the factorial of a given non-negative integer provided as a command-line argument.

Usage:
    python factorial.py <number>

Arguments:
    <number> (int): The non-negative integer for which the factorial will be calculated.

Example:
    python factorial.py 5
    Output: 120

Functions:
    factorial(n):
        Recursively calculates the factorial of a non-negative integer n.
        - If n == 0, returns 1 (base case).
        - Otherwise, returns n * factorial(n-1).

Notes:
    - The script expects a single command-line argument.
    - Input validation (e.g., ensuring the number is non-negative) is not included and should be handled by the user.
    - Factorial of negative numbers is undefined.

"""

import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Ensure a command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Factorial is not defined for negative numbers.")
            sys.exit(1)
        # Calculate and print the factorial
        f = factorial(number)
        print(f"The factorial of {number} is {f}.")
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

