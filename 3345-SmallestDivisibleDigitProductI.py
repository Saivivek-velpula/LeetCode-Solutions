"""
Problem: 3345. Smallest Divisible Digit Product I

Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/

Level: Easy

Description

You are given two integers n and t.

Your task is to find the smallest integer greater than or equal to n such that the product of its digits is divisible by t.

Return the required integer.

Example

Input:

n = 10, t = 2

Output:

10

Explanation:

Product of digits of 10 = 1 × 0 = 0
0 is divisible by 2, so the answer is 10.
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        s = str(n)
        su=1
        for i in s:
            su*=int(i)
        while su%t!=0:
            n+=1
            s = str(n)
            su=1
            for i in s:
                su*=int(i)

        return n