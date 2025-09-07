"""
Problem: 1304. Find N Unique Integers Sum up to Zero
Link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

Level: Easy

Description:
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example:
Input: n = 5
Output: [-7,-1,1,3,4]

"""
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a = []
        if n%2!=0:
            a.append(0)
            n-=1
        i=1
        while n>0:
            a.append(i)
            a.append(i*-1)
            i+=1
            n-=2
        return a