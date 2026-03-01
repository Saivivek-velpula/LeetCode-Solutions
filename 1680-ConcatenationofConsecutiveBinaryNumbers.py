"""
Problem: 1680. Concatenation of Consecutive Binary Numbers
Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

Level: Medium

Description:
You are given an integer n.

Your task is to:

Convert every integer from 1 to n into its binary representation.

Concatenate all these binary strings in order.

Return the decimal value of the resulting binary string.

Since the result can be very large, return it modulo 10⁹ + 7.

Example 1:

Input:

n = 1

Output:

1

Explanation:

Binary of 1 → 1
Concatenated result → 1
Decimal value → 1
"""
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ""
        mod= 10**9 + 7
        for i in range(1,n+1):
            bi = bin(i)[2:]
            s+=bi
        return int(s,2)%mod
