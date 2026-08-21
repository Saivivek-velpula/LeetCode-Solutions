"""
Problem: 2485. Find the Pivot Integer

Link: https://leetcode.com/problems/find-the-pivot-integer/

Level: Easy

Description:

You are given a positive integer n.

Your task is to find the pivot integer x such that:

The sum of all integers from 1 to x is equal to
The sum of all integers from x to n.

In other words:

1 + 2 + ... + x = x + (x + 1) + ... + n

If such an integer exists, return x. Otherwise, return -1.

Example:

Input:

n = 8

Output:

6

Explanation:

For x = 6:

1 + 2 + 3 + 4 + 5 + 6 = 21

6 + 7 + 8 = 21

Since both sums are equal, 6 is the pivot integer.
"""
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in range(1,n+1):
            s+=i
        ps=0
        for i in range(1,n+1):
            ps+=i
            if abs(s-ps)+i == ps:
                return i
        return -1