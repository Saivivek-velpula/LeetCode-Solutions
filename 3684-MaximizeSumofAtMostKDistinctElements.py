"""
Problem: 3684. Maximize Sum of At Most K Distinct Elements

Link: LeetCode - Maximize Sum of At Most K Distinct Elements

Level: Medium

Description:

You are given an integer array nums and an integer k.
Your task is to select at most k distinct elements from the array such that the sum of the selected elements is maximized.

Each chosen element must be distinct.

You can choose fewer than k elements if that yields the maximum sum.

Return the maximum possible sum.

Example 1:

Input:

nums = [5,3,9,9,2]
k = 3


Output:

17


Explanation:

The best choice is {9, 5, 3} → sum = 17.
"""
class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = []
        while k>0 and nums:
            m = max(nums)
            if m in a:
                nums.remove(m)
                continue
            a.append(m)
            k-=1
        return a