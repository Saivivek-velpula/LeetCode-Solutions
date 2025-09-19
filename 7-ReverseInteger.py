"""
Problem: 7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Level: Medium

Description:
Given a signed 32-bit integer x, return its digits reversed.
If the reversed integer overflows outside the 32-bit signed integer range [-2³¹, 2³¹ - 1], return 0.

Example:

Input: x = 123
Output: 321

Input: x = -120
Output: -21
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True
        if x<0:
                flag = False
                x = x*-1 

        ans = 0
        
        while(x!=0):
                r = x%10
                ans = ans*10+r
                x = x//10

        if ans>2**31-1:
            return 0

        if flag == False:
            return ans*-1

        else:
            return ans