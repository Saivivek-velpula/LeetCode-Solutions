"""
Problem: 3718. Smallest Missing Multiple of K

Link: https://leetcode.com/problems/smallest-missing-multiple-of-k/

Level: Easy

Description:

You are given an integer array nums and a positive integer k.

Your task is to find the smallest positive multiple of k that does not appear in nums.

In other words, check the multiples of k starting from k:

k, 2k, 3k, 4k, ...

Return the first multiple that is missing from the array.

Example:

Input:

nums = [8,2,3,4,6]
k = 2

Output:

10

Explanation:

The positive multiples of 2 are:

2, 4, 6, 8, 10, ...
2 → present
4 → present
6 → present
8 → present
10 → missing

Therefore, the smallest missing multiple of 2 is 10.
"""
class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = set(nums)
        m = k
        while m in nums:
            m+=k
        return m