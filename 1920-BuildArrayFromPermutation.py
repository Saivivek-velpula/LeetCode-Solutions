"""
Problem: 1920. Build Array from Permutation
Link: https://leetcode.com/problems/build-array-from-permutation/

Level: Easy

Description:
Given a zero-based permutation nums (an array containing each integer from 0 to 
n-1 exactly once), build an array ans of the same length where ans[i] = nums[nums[i]] 
for each 0 <= i < n.
"""
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans