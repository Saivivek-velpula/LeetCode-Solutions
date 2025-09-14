"""
Problem: 3683. Earliest Time to Finish One Task

Link: LeetCode - Earliest Time to Finish One Task

Level: Easy

Description:

You are given an array time where time[i] represents the amount of time required to finish the i-th task.

You are allowed to pick exactly one task to perform.
Return the minimum time required among all tasks, i.e., the earliest possible finishing time.

Example 1:

Input:

time = [2, 5, 7, 1, 4]


Output:

1


Explanation:

The task requiring 1 unit of time is the fastest to complete.
"""
class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        a = []
        for i in tasks:
            s = sum(i)
            a.append(s)
        return min(a)