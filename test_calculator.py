# https://github.com/sunayk64/lab10-SK-AP
#Partner 1: Sunay Kanade
#Partner 2: Avadhesh Persad

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -7), 4)

    # ##########################

    ######## Partner 1
    def test_multiply(self): 
        self.assertEqual(mul(4, 3), 12)
        self.assertEqual(mul(2, 8), 16)
        self.assertEqual(mul(9, 7), 63)

    def test_divide(self): 
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(16, 4), 4)
        self.assertEqual(div(36, 6), 6)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        with self.assertRaises(ValueError):
            log(-1, 100)

    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)  
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(25), 5.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()