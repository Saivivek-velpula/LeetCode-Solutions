"""
Problem: 3019. Number of Changing Keys
Link: https://leetcode.com/problems/number-of-changing-keys/

Level: Easy

Description:
You are given a string s consisting of only lowercase and uppercase English letters.
A changing key occurs when two consecutive characters in s differ only by case (one is uppercase, the other is lowercase).

Return the total number of changing keys in the string.

Example 1:

Input: s = "aAbBcC"
Output: 5
"""
class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        for i in range(len(s)-1):
            if s[i]!=s[i+1].upper() and s[i]!=s[i+1].lower():
                c+=1
        return c