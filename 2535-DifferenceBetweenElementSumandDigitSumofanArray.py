"""
Problem: 2535. Difference Between Element Sum and Digit Sum of an Array

Link: LeetCode - Difference Between Element Sum and Digit Sum of an Array

Level: Easy

Description:

You are given an integer array nums.

The element sum is the sum of all the numbers in nums.

The digit sum is the sum of all digits of every number in nums.

Return the absolute difference between the element sum and the digit sum.

Example 1:

Input:

nums = [1, 15, 6, 3]


Output:

9


Explanation:

Element sum = 1 + 15 + 6 + 3 = 25

Digit sum = (1) + (1+5) + (6) + (3) = 15

|25 - 15| = 10
"""
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = 0
        s2=0
        for i in nums:
            s1+=i
            while i>0:
                s2 = s2+ i%10
                i = i//10
        return abs(s1-s2)