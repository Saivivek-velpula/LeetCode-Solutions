"""
Problem: 1051. Height Checker
Link: https://leetcode.com/problems/height-checker/

Level: Easy

Description:
A school is taking an annual photo where students must stand in a single line in non-decreasing order of height.
You are given an array heights representing the current order of students.

Create an array expected by sorting heights in non-decreasing order and return the number of indices where
heights[i] is not equal to expected[i].

Example:
Input: heights = [1,1,4,2,1,3]
Output: 3

"""
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        a = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                count+=1
        return count