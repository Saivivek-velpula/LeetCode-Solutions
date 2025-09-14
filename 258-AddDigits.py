"""
Problem: 258. Add Digits

Link: LeetCode - Add Digits

Level: Easy

Description:

Given an integer num, repeatedly add all its digits until the result has only one digit.

Return the final single-digit result.

Example 1:

Input:

num = 38


Output:

2


Explanation:

3 + 8 = 11 → still has 2 digits

1 + 1 = 2 → single digit reached

Answer = 2
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            val = 0
            n = num
            while n>0:
                val = val + n%10
                n = n//10
            num = val
        return num