"""
Problem: 1752. Check if Array Is Sorted and Rotated
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Level: Easy

Description:
You are given an integer array nums.

An array is considered sorted and rotated if:

It was originally sorted in non-decreasing order, and

It was rotated some number of times (possibly zero times).

A rotation means moving the first element of the array to the end.
This operation can be performed any number of times.

Your task is to return true if the given array nums can be obtained by rotating a non-decreasing sorted array. Otherwise, return false.

Example 1:

Input:

nums = [3,4,5,1,2]


Output:

true


Explanation:

The original sorted array is:

[1,2,3,4,5]


After rotating it 3 times, we get:

[3,4,5,1,2]


So return true.

Example 2:

Input:

nums = [2,1,3,4]


Output:

false


Explanation:

There is no sorted array that can be rotated to form [2,1,3,4].

So return false.

Example 3:

Input:

nums = [1,2,3]


Output:

true


Explanation:

The array is already sorted.
Rotation by 0 times is valid.

So return true.
"""
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        i=1
        while i<len(nums):
            if nums[i]<nums[i-1]:
                c+=1
            if c>1:
                return False
            i+=1
        if nums[i-1]>nums[0]:
            c+=1
        if c>1:
            return False
        return True