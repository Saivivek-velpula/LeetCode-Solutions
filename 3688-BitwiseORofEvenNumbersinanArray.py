"""
Problem: 3688. Bitwise OR of Even Numbers in an Array
Link: https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

Level: Easy

Description:
You are given an integer array nums. Return the bitwise OR of all even numbers in the array.

If there are no even numbers, return 0.

The bitwise OR operation takes the binary representation of numbers and performs OR on each corresponding bit.

Example:

Input: nums = [3,5,6,2,7]
Output: 6
Explanation: Even numbers = [6,2], and 6 | 2 = 6.
"""
class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            if i%2==0:
                a=a|i
        return a