"""
Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

Level: Easy

Description:

You are given a 0-indexed integer array nums.

First, find the sequential prefix sum of the array. A sequential prefix is formed by starting from nums[0] and continuing while every next element is exactly 1 greater than the previous element.

Calculate the sum of this sequential prefix.

Then, find the smallest integer greater than or equal to this sum that does not appear in nums.

Return that integer.

Example:

Input:

nums = [1,2,3,2,5]

Output:

7

Explanation:

The sequential prefix is [1,2,3].
Its sum is 1 + 2 + 3 = 6.
Starting from 6, check which number is missing from nums.
6 is not present in nums.
Therefore, the answer is 6.
"""

class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s=nums[0]
        for i in range(1,len(nums)):
            if nums[i]== nums[i-1]+1:
                s+=nums[i]
            else:
                break
        while s in nums:
            s+=1
        return s