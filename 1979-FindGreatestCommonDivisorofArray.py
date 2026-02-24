"""Problem: 1979. Find Greatest Common Divisor of Array
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Level: Easy

Description:
You are given an integer array nums.

Your task is to find the greatest common divisor (GCD) of the smallest and largest numbers in the array.

The greatest common divisor (GCD) of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

Return the GCD of the minimum element and the maximum element in nums.

Example 1:

Input:

nums = [2,5,6,9,10]

Output:

2

Explanation:

Minimum value = 2

Maximum value = 10

GCD(2, 10) = 2

Return 2.
"""
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = max(nums)
        mi = min(nums)
        gcd = 0
        for i in range(1,mi+1):
            if ma%i==0 and mi%i==0:
                gcd = max(gcd,i)
        return gcd