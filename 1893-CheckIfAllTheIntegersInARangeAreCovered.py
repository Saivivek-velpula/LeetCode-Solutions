"""
Problem: 1893. Check if All the Integers in a Range Are Covered
Link: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

Level: Easy

Description:
You are given a 2D integer array ranges where ranges[i] = [start_i, end_i] represents an inclusive interval of integers.

You are also given two integers left and right.

Your task is to determine whether every integer in the range [left, right] is covered by at least one interval in ranges.

An integer x is considered covered if there exists at least one interval [start_i, end_i] such that:

start_i ≤ x ≤ end_i


Return true if all integers from left to right (inclusive) are covered. Otherwise, return false.

Example 1:

Input:

ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5


Output:

true


Explanation:

The numbers in the range [2,5] are: 2, 3, 4, 5

2 is covered by [1,2]

3 and 4 are covered by [3,4]

5 is covered by [5,6]

All numbers are covered → return true

Example 2:

Input:

ranges = [[1,10],[10,20]]
left = 21
right = 21


Output:

false


Explanation:

21 is not covered by any interval → return false
"""
class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        d = {}
        for i in range(left,right+1):
            if i in d:
                d[i]+=1
            else:
                d[i]=0
        for i in ranges:
            start = i[0]
            end = i[1]
            for x in range(left,right+1):
                if x>=start and x<=end:
                    d[x]+=1
        for i in d:
            if d[i]==0:
                return False
        return True