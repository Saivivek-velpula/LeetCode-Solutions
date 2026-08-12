"""
Problem: 15. 3Sum

Link: https://leetcode.com/problems/3sum/

Level: Medium

Description:

You are given an integer array nums.

Your task is to find all unique triplets [nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] == 0

The solution must not contain duplicate triplets.

Return the result as a 2D array of all valid triplets.

Example:

Input:

nums = [-1,0,1,2,-1,-4]

Output:

[[-1,-1,2],[-1,0,1]]

Explanation:

The valid triplets whose sum is 0 are:

-1 + (-1) + 2 = 0
-1 + 0 + 1 = 0

Duplicate triplets are not included in the answer.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans= []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1

            while j<k:
                target = nums[i]+nums[j]+nums[k]
                if target==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while nums[k]==nums[k+1] and j<k:
                        k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif target>0:
                    k-=1
                else:
                    j+=1
            
        return ans