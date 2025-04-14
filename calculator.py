"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""

import math

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0: 
        raise ZeroDivisionError
    return b/a

def log(a, b):
    try:
        return math.log(b, a)
    except: 
        raise ValueError

def exp(a, b):
    return a ** b



