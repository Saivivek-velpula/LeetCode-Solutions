"""
Problem: 3158. Find the XOR of Numbers Which Appear Twice
Link: https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

Level: Easy

Description:
You are given an integer array nums.
Find the XOR of all numbers that appear exactly twice in the array.

If no number appears twice, return 0.

Example:

Input: nums = [1,2,1,3]
Output: 1


Explanation:

The only number that appears exactly twice is 1.

So, result = 1.

"""

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        val = 0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==2:
                val = val^i
        return val