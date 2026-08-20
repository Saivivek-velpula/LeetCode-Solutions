"""
Problem: 1863. Sum of All Subset XOR Totals

Link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/

Level: Easy

Description:

You are given an integer array nums.

The XOR total of an array is defined as the bitwise XOR of all its elements. If the array is empty, its XOR total is 0.

Your task is to find the sum of the XOR totals of every possible subset of nums.

A subset can contain any number of elements, including the empty subset.

Example:

Input:

nums = [1,3]

Output:

6

Explanation:

All possible subsets are:

[]
[1]
[3]
[1,3]

Their XOR totals are:

[]       → 0
[1]      → 1
[3]      → 3
[1,3]    → 1 XOR 3 = 2

Therefore:

0 + 1 + 3 + 2 = 6
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        def solve(i,temp):
            if i>=len(nums):
                res.append(list(temp))
                return
            temp.append(nums[i])
            solve(i+1,temp)
            temp.pop()
            solve(i+1,temp)
        solve(0,[])
        x=0
        for i in res:
            r=0
            for j in i:
                r=r^j
            x+=r
        return x