"""
Problem: 3622. Check Divisibility by Digit Sum and Product

Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

Level: Easy

Description:

You are given a positive integer n.

Your task is to determine whether n is divisible by both:

The sum of its digits
The product of its digits

Return true if both conditions are satisfied. Otherwise, return false.

Example:

Input:

n = 99

Output:

true

Explanation:

The digits of 99 are 9 and 9.

Digit Sum:

9 + 9 = 18

Digit Product:

9 × 9 = 81

Since:

99 % 18 != 0

Actually, 99 is not divisible by its digit sum, so the result is:

false
"""
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        return (n%(s+p))==0