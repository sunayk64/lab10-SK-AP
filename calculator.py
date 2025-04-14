"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""

import math

def square_root(a):
    try: 
        if a < 0: 
            raise ValueError
        return math.sqrt(a)
    except:
        raise ValueError
    
def hypotenuse(a, b):
    try: 
        return math.hypot(a, b)
    except:
        raise ValueError

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



