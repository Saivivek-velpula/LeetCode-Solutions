"""
Problem: 350. Intersection of Two Arrays II
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Level: Easy

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result should appear as many times as it shows in both arrays, and you may return the result in any order.

Example:
Input:
nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2,2]
"""
class Solution:
    def intersect(self, nums1, nums2):
        a =[]
        for i in nums1:
            if i in nums2:
                a.append(i)
                nums2.remove(i)
        return a