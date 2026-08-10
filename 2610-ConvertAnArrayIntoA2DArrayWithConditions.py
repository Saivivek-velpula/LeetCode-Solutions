"""
Problem: 2610. Convert an Array Into a 2D Array With Conditions

Link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

Level: Medium

Description:

You are given an integer array nums.

Your task is to convert the array into a 2D array such that:

Each row contains distinct integers.
The number of rows should be as small as possible.
Every element from nums must be included in the resulting 2D array.

In other words, if an element appears multiple times in nums, its occurrences must be placed in different rows.

Example:

Input:

nums = [1,3,4,1,2,3,1]

Output:

[[1,3,4,2],[1,3],[1]]

Explanation:

Each row contains only distinct elements.
The number 1 appears 3 times, so at least 3 rows are required.
The number 3 appears 2 times, so it can be placed in any 2 of those rows.
Therefore, the minimum number of rows is 3.
"""

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n = len(nums)
        res=[]
        while n>0:
            a=[]
            for i in d:
                if d[i]!=0 and (i not in a):
                    a.append(i)
                    d[i]-=1
                    n-=1
            res.append(a)
        return res