"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""

import math

# First example
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0: 
        raise ZeroDivisionError
    return b/a

def logarithm(a, b):
    try:
        return math.log(b, a)
    except: 
        raise ValueError

def exponent(a, b):
    return a ** b



