"""
Problem: 11. Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water/

Level: Medium

Description:

You are given an integer array height where each element represents the height of a vertical line.

The lines are drawn at different positions, and together with the x-axis, they form a container.

Your task is to find the maximum amount of water that can be stored between any two lines.

The amount of water is calculated as:

width × minimum(height[left], height[right])
Example:

Input:

height = [1,8,6,2,5,4,8,3,7]

Output:

49

Explanation:

Choose the lines with heights 8 and 7.

Width = 8 - 1 = 7
Minimum height = min(8, 7) = 7

Area = 7 * 7 = 49

Therefore, the maximum amount of water that can be stored is 49.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m=0
        i=0
        j=len(height)-1
        while i<=j:
            if height[i]<height[j]:
                m= max(m,height[i]*(j-i))
                i+=1
            else:
                m= max(m,height[j]*(j-i))
                j-=1
        return m