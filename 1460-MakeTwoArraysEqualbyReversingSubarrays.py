"""
Problem: 1460. Make Two Arrays Equal by Reversing Subarrays
Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

Level: Easy

Description:
You are given two integer arrays target and arr of the same length.

In one operation, you can choose any non-empty subarray of arr and reverse it. You can perform this operation any number of times.

Return true if it is possible to make arr equal to target, otherwise return false.

Example 1:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true

Example 2:
Input: target = [7], arr = [7]
Output: true

Example 3:
Input: target = [3,7,9], arr = [3,7,11]
Output: false
"""

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        t = sorted(target)
        a = sorted(arr)
        for i in range(len(a)):
            if t[i]!=a[i]:
                return False
        return True