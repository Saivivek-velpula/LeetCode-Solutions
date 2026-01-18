"""
Problem: 1184. Distance Between Bus Stops
Link: https://leetcode.com/problems/distance-between-bus-stops/

Level: Easy

Description:
A circular bus route has n stops numbered from 0 to n - 1.
You are given an array distance where distance[i] represents the distance between stop i and stop (i + 1) % n.

The bus can travel in both clockwise and counterclockwise directions.

Given two stops start and destination, return the shortest distance required to travel between them.

Example:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
"""
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        clock = 0
        i = start
        while i!=destination:
            clock+=distance[i]
            if i== len(distance)-1:
                i=0
            else:
                i+=1
        anclock = 0
        j = start
        while j!=destination:
            if j<=0:
                j = len(distance)-1
            else:
                j-=1
            anclock+=distance[j]
            
        return min(clock,anclock)