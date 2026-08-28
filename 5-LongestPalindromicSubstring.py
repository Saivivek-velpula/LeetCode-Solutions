"""
Problem: 5. Longest Palindromic Substring

Link: https://leetcode.com/problems/longest-palindromic-substring/

Level: Medium

Description:

You are given a string s.

Your task is to find the longest palindromic substring in s.

A palindrome is a string that reads the same forward and backward.

A substring is a contiguous sequence of characters within the string.

If there are multiple palindromic substrings with the same maximum length, returning any one of them is acceptable.

Example:

Input:

s = "babad"

Output:

"bab"

Explanation:

Both "bab" and "aba" are valid palindromic substrings of maximum length 3.

Therefore, "bab" can be returned as the answer.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns=""
        l=0
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
        
            return s[left+1:right]

        for i in range(len(s)):
            p1=expand(i,i)
            p2=expand(i,i+1)
            if len(p1)>l:
                l=len(p1)
                ns=p1
            if len(p2)>l:
                l=len(p2)
                ns=p2
            
        return ns