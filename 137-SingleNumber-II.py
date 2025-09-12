"""
Problem: 137. Single Number II
Link: https://leetcode.com/problems/single-number-ii/

Level: Medium

Description:
You are given a non-empty array of integers nums, where every element appears three times except for one, which appears exactly once.

Find and return the element that appears only once.

Your algorithm should have a linear runtime complexity and use only constant extra space.

Example:

Input: nums = [2,2,3,2]
Output: 3

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i] == 1:
                return i