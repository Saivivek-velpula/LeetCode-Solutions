"""
Problem: 50. Pow(x, n)
Link: https://leetcode.com/problems/powx-n/

Level: Medium

Description:
Implement the function pow(x, n), which calculates x raised to the power n (xⁿ).

x is a floating-point number.

n is an integer (can be negative, zero, or positive).

You must implement the function with O(log n) time complexity.

Example:

Input: x = 2.00000, n = 10
Output: 1024.00000

"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n