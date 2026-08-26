"""
Problem: 2904. Shortest and Lexicographically Smallest Beautiful String

Link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

Level: Medium

Description:

You are given a binary string s and an integer k.

A string is called beautiful if it contains exactly k occurrences of the character '1'.

Your task is to find the shortest beautiful substring of s.

If there are multiple beautiful substrings with the same minimum length, return the lexicographically smallest one.

If no beautiful substring exists, return an empty string.
"""
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ns=""
        i=0
        c=0
        l=len(s)
        for j in range(len(s)):
            if s[j]=="1":
                c+=1
            while (c>k and i<j):
                if s[i]=="1":
                    c-=1
                i+=1

            if c == k:

                while s[i] == "0":
                    i += 1

                current = s[i:j+1]

                if len(current) < l:
                    ns = current
                    l = len(current)

                elif len(current) == l and current < ns:
                    ns = current

        if c==k and ns=="":
            return s
        return ns

        