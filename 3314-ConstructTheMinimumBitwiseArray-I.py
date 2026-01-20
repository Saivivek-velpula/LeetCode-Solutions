"""
Problem: 3314. Construct the Minimum Bitwise Array I
Link: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

Level: Easy

Description:
You are given an array nums consisting of n prime integers.

Your task is to construct an array ans of length n such that for each index i:

ans[i] OR (ans[i] + 1) == nums[i]


Among all possible values that satisfy the condition, choose the minimum possible value for each ans[i].

If no such value exists for a given index, set ans[i] = -1.

Example:

Input:

nums = [2,3,5,7]


Output:

[-1,1,4,3]


Explanation:

For nums[0] = 2, no value of ans[0] satisfies the condition → -1

For nums[1] = 3, smallest valid value is 1 → 1 OR 2 = 3

For nums[2] = 5, smallest valid value is 4 → 4 OR 5 = 5

For nums[3] = 7, smallest valid value is 3 → 3 OR 4 = 7
"""
class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            j = 1
            flag = 0
            while j<i:
                if (j | j+1) == i:
                    a.append(j)
                    flag = 1
                    break
                j+=1
            if flag == 0:
                a.append(-1) 
        return a