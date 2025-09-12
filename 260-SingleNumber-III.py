"""
Problem: 260. Single Number III
Link: https://leetcode.com/problems/single-number-iii/

Level: Medium

Description:
You are given an integer array nums where exactly two elements appear only once, and all the other elements appear exactly twice.

Return the two elements that appear only once.
You may return the answer in any order.

Example:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d ={}
        a =[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for i in d:
            if d[i] == 1:
                a.append(i)
        return a