"""Problem: 1913. Maximum Product Difference Between Two Pairs
Link: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

Level: Easy

Description:
You are given an integer array nums.

Your task is to choose four distinct indices w, x, y, and z such that the product difference between two pairs is maximized.

The product difference is defined as:

(nums[w] * nums[x]) - (nums[y] * nums[z])


Return the maximum possible product difference.

🔎 Important Conditions:

All four indices must be different.

You must form two pairs:

One pair whose product is as large as possible.

One pair whose product is as small as possible.

Example 1:

Input:

nums = [5,6,2,7,4]


Output:

34


Explanation:

Choose:

Largest pair → 7 and 6 → 7 × 6 = 42

Smallest pair → 2 and 4 → 2 × 4 = 8

Product difference:

42 - 8 = 34


Return 34.

Example 2:

Input:

nums = [4,2,5,9,7,4,8]


Output:

64


Explanation:

Choose:

Largest pair → 9 and 8 → 72

Smallest pair → 2 and 4 → 8

Product difference:

72 - 8 = 64


Return 64.
"""
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums= sorted(nums)
        val = (nums[-1]*nums[-2])-(nums[0]*nums[1])
        return val