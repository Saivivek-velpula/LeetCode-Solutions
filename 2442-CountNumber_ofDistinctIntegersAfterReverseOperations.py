"""
Problem: 2442. Count Number of Distinct Integers After Reverse Operations
Link: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

Level: Medium

Description:
You are given an integer array nums. For each integer in nums, you may reverse its digits (e.g., 123 → 321).
After performing this reverse operation on every number, add both the original and reversed numbers into a collection.

Return the total number of distinct integers present in the collection.

Example:

Input: nums = [1,13,10,12,31]
Output: 6
Explanation:  
- Reverse(1) = 1  
- Reverse(13) = 31  
- Reverse(10) = 1  
- Reverse(12) = 21  
- Reverse(31) = 13  

Final distinct numbers = {1, 13, 10, 12, 31, 21} → 6
"""
class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        for i in num:
            n = i
            rev = 0
            while n>0:
                rev = rev*10 + n%10
                n = n//10
            nums.append(rev)
        a = set(nums)
        return len(a)