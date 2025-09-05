"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Level: Easy

Description:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d1={}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in d1:
                return [i,d1[dif]]
            else:
                d1[nums[i]]=i
