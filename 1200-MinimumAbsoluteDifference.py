"""
Problem: 1200. Minimum Absolute Difference
Link: https://leetcode.com/problems/minimum-absolute-difference/

Level: Easy

Description:
Given an array of distinct integers arr, find all pairs of elements that have the minimum absolute difference among all possible pairs.

Each returned pair [a, b] must satisfy:

a and b are elements from arr

a < b

b - a equals the minimum absolute difference in the array

Return the list of pairs in ascending order.

Example:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
"""
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        d = arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<d:
                d=arr[i+1]-arr[i]
        a = []
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==d:
                a.append([arr[i],arr[i+1]])
        return a