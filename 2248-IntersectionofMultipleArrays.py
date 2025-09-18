"""
Problem: 2248. Intersection of Multiple Arrays
Link: https://leetcode.com/problems/intersection-of-multiple-arrays/

Level: Easy

Description:
You are given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers.
Return the intersection of all the arrays contained in nums as a sorted list in ascending order.

Example:
Input:
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

Output:
[3,4]
"""
"""approach 1 : using array"""
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        a =[]
        a1 = nums[0]
        nums.remove(a1)
        for i in a1:
            c = len(nums)
            for j in nums:
                if i in j :
                    c-=1
            if c==0:
                a.append(i)
        a=sorted(a)
        return a

"""approach 2 : using hashtable"""
class Solution:
    def intersection(self, nums):
        a =[]
        d={}
        for i in nums:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        l = len(nums)
        for i in d:
            if d[i]==l:
                a.append(i)
        a= sorted(a)
        return a