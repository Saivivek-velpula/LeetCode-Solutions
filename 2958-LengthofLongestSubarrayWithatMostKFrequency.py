"""
Problem: 2958. Length of Longest Subarray With at Most K Frequency

Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

Level: Medium

Description:

You are given an integer array nums and an integer k.

Your task is to find the length of the longest subarray in which the frequency of every element is at most k.

In other words, no element can appear more than k times within the selected subarray.

Example:

Input:

nums = [1,2,3,1,2,3,1,2]
k = 2

Output:

6

Explanation:

The longest valid subarray is:

[1,2,3,1,2,3]

The frequencies are:

1 → 2 times
2 → 2 times
3 → 2 times

Since every element appears at most 2 times, the length of the subarray is 6.

"""

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        i=0
        j=0
        l=0
        while j<len(nums):
            if nums[j] in d:
                while d[nums[j]]+1>k and i<=j:
                    d[nums[i]]-=1
                    i+=1
                d[nums[j]]+=1
            else:
                d[nums[j]]=1
            
            l=max(j-i+1,l)
            j+=1
        
        return l
                