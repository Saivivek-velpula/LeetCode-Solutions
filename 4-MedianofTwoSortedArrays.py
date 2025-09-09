"""
Problem: 4. Median of Two Sorted Arrays
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Level: Hard

Description:
You are given two sorted arrays nums1 and nums2 of size m and n.
Return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

"""

""" approach:1 using Binary Search """
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = 0
        for i in nums2:
            h = len(nums1)-1
            while l<=h:
                mid = (l+h)//2
                if nums1[mid] > i:
                    h = mid-1
                else:
                    l = mid+1
            nums1.insert(l,i)
        n = len(nums1)
        if n%2 == 0:
            return (nums1[(n/2)-1] + nums1[((n/2)+1)-1])/2.0
        else:
            return nums1[((n+1)/2)-1]
        
"""appraoch:2 Sort Built-in function"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        n = len(nums1)
        if n%2 == 0:
            return (nums1[(n/2)-1] + nums1[((n/2)+1)-1])/2.0
        else:
            return nums1[((n+1)/2)-1]