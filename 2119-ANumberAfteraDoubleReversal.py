"""
Problem: 2119. A Number After a Double Reversal
Link: https://leetcode.com/problems/a-number-after-a-double-reversal/

Level: Easy

Description:
Given a non-negative integer num, reverse its digits once, then reverse the result again.
Return true if the number is the same after performing the double reversal, otherwise return false.

Key Insight:

Any number without trailing zeros remains unchanged after a double reversal.

Numbers ending with zero(s) will not remain the same, except for 0 itself.

Example:

Input: num = 526
Output: true

Input: num = 1800
Output: false

Input: num = 0
Output: true
"""
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        rev = 0
        n = num
        while n>0:
            rev = rev*10 + n%10
            n=n//10
        m = 0
        while rev>0:
            m = m*10+ rev%10
            rev = rev//10
        return num == m