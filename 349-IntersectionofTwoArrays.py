"""
Problem: 349. Intersection of Two Arrays
Link: https://leetcode.com/problems/intersection-of-two-arrays/

Level: Easy

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique, and you may return the result in any order.

Example:
Input:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2]
"""
"""approach 1: using array"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums1:
            if i in nums2 and i not in a:
                a.append(i)
        return a
"""approach 2: using & operator"""
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))