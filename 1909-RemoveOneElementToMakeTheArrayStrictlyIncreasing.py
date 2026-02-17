"""
Problem: 1909. Remove One Element to Make the Array Strictly Increasing
Link: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

Level: Easy

Description:
You are given a 0-indexed integer array nums.

Your task is to determine whether it is possible to remove exactly one element from the array so that the remaining elements form a strictly increasing array.

An array is considered strictly increasing if for every index i (where 0 ≤ i < n - 1):

nums[i] < nums[i + 1]


Return true if you can remove exactly one element to make the array strictly increasing. Otherwise, return false.

Example 1:

Input:

nums = [1,2,10,5,7]


Output:

true


Explanation:

By removing 10, the array becomes:

[1,2,5,7]


This is strictly increasing.
So return true.

Example 2:

Input:

nums = [2,3,1,2]


Output:

false


Explanation:

Removing any single element will not make the array strictly increasing.
So return false.

Example 3:

Input:

nums = [1,1,1]


Output:

false


Explanation:

Removing one element still leaves duplicate values, so the array is not strictly increasing.
So return false.
"""
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(len(nums)):
            flag= 0
            a = []
            for j in range(len(nums)):
                if i!=j:
                    a.append(nums[j])
            for k in range(1,len(a)):
                if a[k-1]>=a[k]:
                    flag=1
                    break
            if flag==0:
                return True
        return False