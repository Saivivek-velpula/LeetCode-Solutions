"""Problem: 1967. Number of Strings That Appear as Substrings in Word
Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

Level: Easy

Description:
You are given:

An array of strings patterns

A string word

Your task is to determine how many strings in patterns appear as a substring of word.

A string pattern is considered a substring of word if it appears as a continuous sequence of characters inside word.

Return the total number of strings in patterns that are substrings of word.

Example 1:

Input:

patterns = ["a","abc","bc","d"]
word = "abc"

Output:

3

Explanation:

"a" appears in "abc"

"abc" appears in "abc"

"bc" appears in "abc"

"d" does not appear

Total = 3"""
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        c=0
        for i in patterns:
            if i in word:
                c+=1
        return c