"""
Problem: 2160. Minimum Sum of Four Digit Number After Splitting Digits

Link: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

Level: Easy

Description:

You are given a four-digit positive integer num.

Your task is to split the four digits into two two-digit integers and find the minimum possible sum of these two numbers.

Each digit must be used exactly once.

Example:

Input:

num = 2932

Output:

52

Explanation:

The digits are:

2, 9, 3, 2

The minimum sum can be obtained by forming:

23 + 29 = 52

Therefore, the minimum possible sum is 52.
"""
class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        ns = s[0]+s[2]
        ns2 = s[1]+s[3]
        return int(ns)+int(ns2)