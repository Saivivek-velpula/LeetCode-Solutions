"""
Problem: 3857. Minimum Cost to Split into Ones
Link: https://leetcode.com/problems/minimum-cost-to-split-into-ones/

Level: Easy

Description:
You are given a binary string s consisting only of characters '0' and '1'.

You can perform operations to split the string into segments so that eventually every segment contains only the character '1'.

Each split operation has a certain cost (as defined in the problem).

Your task is to determine the minimum total cost required to split the string so that all remaining segments contain only '1'.

Return the minimum possible cost.

Example 1:

Input:

s = "1101"

Output:

1

Explanation:
By performing one optimal split, we can separate the '0' and obtain segments that contain only '1'.
Minimum cost = 1.
"""
class Solution(object):
    def minCost(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = n-1
        s = b
        while b>1:
            b = b-1
            s+=b
        return s