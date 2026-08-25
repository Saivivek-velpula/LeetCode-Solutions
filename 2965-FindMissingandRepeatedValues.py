"""
Problem: 2965. Find Missing and Repeated Values

Link: https://leetcode.com/problems/find-missing-and-repeated-values/

Level: Easy

Description:

You are given an n x n integer matrix grid containing numbers from 1 to n².

However, one number appears twice, while another number is missing.

Your task is to find the repeated number and the missing number.

Return them as an array:

[repeated, missing]
Example:

Input:

grid = [[1,3],
        [2,2]]

Output:

[2,4]

Explanation:

The numbers from 1 to 4 should be:

1, 2, 3, 4

But the grid contains:

1, 3, 2, 2
2 appears twice → Repeated value = 2
4 does not appear → Missing value = 4

Therefore, the answer is:

[2,4]
"""
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        d={}
        for i in grid:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        m=0
        r=0
        n=len(grid)
        for i in range(1,n*n+1):
            if (i in d) and d[i]>1:
                r=i
            elif m!=0 and r!=0:
                break
            elif i not in d:
                m=i
        return [r,m]