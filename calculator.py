# https://github.com/sunayk64/lab10-SK-AP
#Partner 1: Sunay Kanade
#Partner 2: Avadhesh Persad

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

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0: 
        raise ZeroDivisionError
    return b/a

def logarithm(a, b):
    try:
        return math.log(b, a)
    except: 
        raise ValueError

def exp(a, b):
    return a ** b



