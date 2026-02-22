"""Problem: 868. Binary Gap
Link: https://leetcode.com/problems/binary-gap/

Level: Easy

Description:
You are given a positive integer n.

The binary gap of n is the maximum distance between two consecutive 1s in its binary representation.

Return the largest distance between any two adjacent 1s.
If there are fewer than two 1s, return 0.

Example 1:

Input:

n = 22

Output:

2
"""
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = bin(n)[2:]
        m = 0
        f = -1
        s = -1
        for i in range(len(bits)):
            if bits[i]=="1":
                if f==-1:
                    f=i
                else:
                    s=i
            if f!=-1 and s!=-1:
                diff = s-f
                m = max(m,diff)
                f=s
                s=-1
        return m