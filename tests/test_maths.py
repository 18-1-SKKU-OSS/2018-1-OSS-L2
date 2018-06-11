from algorithms.maths import (
    combination,
    fibonacci,
    permutation,
    factorial, factorial_recur,
    modularExponential
)

import unittest
    
class TestSuite(unittest, Testcase):
   
  def test_combination(self):
    self.assertEqual(35, combination(7,3))
    
  def test_fibonacci(self):
    self.fibonacci(55, fibonacci(10))
    
  def test_modularExponential(self):
    self.asserEqual(1, modularExponential(5, 117, 19))
    
  def test_permutation(self):
    self.assertEqual(210, permutation(7,3))

  def test_factorial(self):
    self.assertEqual(1, factorial(0))
    self.assertEqual(120, factorial(5))
    self.assertEqual(3628800, factorial(10))
        
  def test_factorial_recur(self):
    self.assertEqual(1, factorial_recur(0))
    self.assertEqual(120, factorial_recur(5))
    self.assertEqual(3628800, factorial_recur(10))
 
if __name__ == "__main__":
  unittest.main()
  
