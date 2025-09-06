"""Problem: 387. First Unique Character in a String
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Level: Easy

Description:
Given a string s, find the first non-repeating character in it and return its index.  
If it does not exist, return -1.

Example:
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1

"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            if d[i]==1:
                return s.index(i)
        return -1