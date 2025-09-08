"""
Problem: 1317. Convert Integer to the Sum of Two No-Zero Integers
Link: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

Level: Easy

Description:
A no-zero integer is a positive integer that does not contain the digit 0.

Given an integer n, return a list of two integers [a, b] such that:

a + b = n

Both a and b are no-zero integers

It is guaranteed that at least one valid solution exists. If there are multiple answers, return any of them.

Example:
Input: n = 11
Output: [2, 9]
Explanation: 2 + 9 = 11, and both 2 and 9 do not contain the digit 0.

"""

class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            a = i
            b = n-i
            if '0' in str(a) or '0' in str(b):
                continue
            if a+b==n:
                return a,b
        