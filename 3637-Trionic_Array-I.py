"""
Problem: 3637. Trionic Array I
Link: https://leetcode.com/problems/trionic-array-i/

Level: Easy

Description:
You are given an integer array nums of length n.

An array is called trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing

nums[p...q] is strictly decreasing

nums[q...n − 1] is strictly increasing

Return true if nums is trionic, otherwise return false.

Example:
Input: nums = [1,3,5,4,2,6]
Output: true

Explanation:
Choose p = 2, q = 4

nums[0...2] = [1, 3, 5] → strictly increasing

nums[2...4] = [5, 4, 2] → strictly decreasing

nums[4...5] = [2, 6] → strictly increasing
"""
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = 0
        q = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i+1]<nums[i]:
                p=i
                break
            if nums[i+1]==nums[i]:
                return False
        if p==0:
            return False
        for i in range(p,n-1):
            if nums[i+1]>nums[i]:
                q=i
                break
            if nums[i+1]==nums[i]:
                return False
        if q==n-1 or p==q:
            return False
        for i in range(q,n-1):
            if nums[i+1]<nums[i]:
                return False
            if nums[i+1]==nums[i]:
                return False
        return True