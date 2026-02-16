"""
Problem: 2124. Check if All A's Appears Before All B's
Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

Level: Easy

Description:
You are given a string s consisting only of characters 'a' and 'b'.

Your task is to determine whether all the characters 'a' appear before any character 'b' in the string.

Return true if the condition is satisfied. Otherwise, return false.

In other words, once a 'b' appears in the string, there should not be any 'a' after it.

Example 1:

Input:

s = "aaabbb"


Output:

true


Explanation:

All 'a' characters come before any 'b'.
So return true.

Example 2:

Input:

s = "abab"


Output:

false


Explanation:

There is an 'a' after a 'b'.
So the condition is violated → return false.

Example 3:

Input:

s = "bbb"


Output:

true


Explanation:

There are no 'a' characters.
The condition is still satisfied.

So return true.
"""
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=0
        for i in range(len(s)-1):
            if s[i] == 'b'and s[i+1]=='a':
                return False
        return True