"""
Problem: 1935. Maximum Number of Words You Can Type
Link: https://leetcode.com/problems/maximum-number-of-words-you-can-type/

Level: Easy

Description:
There is a malfunctioning keyboard where some letter keys do not work. You are given a text string text consisting of words separated by single spaces and a string brokenLetters consisting of distinct letters.

A word can be typed only if it does not contain any broken letters.
Return the number of words in text that can be fully typed using the working keys.

Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: Only "world" can be typed because "hello" contains the broken letter 'a'.
"""

""" approach 1: using hash table"""
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        d = {}
        j=1
        for i in text:
            if i == " ":
                j+=1
            elif j in d:
                d[j]+=i
            else:
                d[j]=i
        c = len(d)
        for i in d:
            for k in brokenLetters:
                if k in d[i]:
                    c-=1
                    break
        return c

"""approach 2 : using string variable"""
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        c = text.count(" ")+1
        s = ""
        for i in text:
            if i ==" ":
                for i in brokenLetters:
                    if i in s:
                        s = ""
                        c-=1
                s=""
            else:
                s+=i
        if s!="":
            for i in brokenLetters:
                if i in s:
                    c-=1
                    break 
        return c
                    