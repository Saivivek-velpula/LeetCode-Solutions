"""
Problem: 3856. Trim Trailing Vowels
Link: https://leetcode.com/problems/trim-trailing-vowels/

Level: Easy

Description:
You are given a string s consisting of lowercase English letters.

Your task is to remove all trailing vowels from the string.

A vowel is any of the following characters:
'a', 'e', 'i', 'o', 'u'.

Trailing vowels are the vowels that appear consecutively at the end of the string.

Return the resulting string after removing all trailing vowels.

Example 1:

Input:

s = "leetcode"

Output:

"leetcod"

Explanation:
The string ends with 'e', which is a vowel.
Remove it → "leetcod".
"""
class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)-1,-1,-1):
            if s[i] not in "aeiou":
                res = s[:i+1]
                break
        return res