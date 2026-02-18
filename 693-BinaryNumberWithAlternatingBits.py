"""
Problem: 693. Binary Number with Alternating Bits
Link: https://leetcode.com/problems/binary-number-with-alternating-bits/

Level: Easy

Description:
You are given a positive integer n.

Your task is to determine whether its binary representation has alternating bits.

A binary number has alternating bits if no two adjacent bits are the same.
In other words, every pair of neighboring bits must be different (either 0 followed by 1, or 1 followed by 0).

Return true if n has alternating bits. Otherwise, return false.

Example 1:

Input:

n = 5


Output:

true


Explanation:

Binary representation of 5 is:

101


The bits alternate (1 → 0 → 1), so return true.

Example 2:

Input:

n = 7


Output:

false


Explanation:

Binary representation of 7 is:

111


Adjacent bits are the same, so return false.

Example 3:

Input:

n = 11


Output:

false


Explanation:

Binary representation of 11 is:

1011


The last two bits are both 1, so the bits are not alternating.
Return false.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)[2:]
        for i in range(len(bits)-1):
            if bits[i]==bits[i+1]:
                return False
        return True