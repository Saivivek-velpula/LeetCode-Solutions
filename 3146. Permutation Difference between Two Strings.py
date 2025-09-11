"""
Problem: 3146. Permutation Difference between Two Strings
Link: https://leetcode.com/problems/permutation-difference-between-two-strings/

Level: Easy

Description:
You are given two strings s and t, which are permutations of each other.
The permutation difference between s and t is defined as the sum of the absolute differences between the positions of the same character in s and t.

Return the permutation difference between the two strings.

Example:

Input: s = "abc", t = "bac"
Output: 2


Explanation:

'a' is at index 0 in s and index 1 in t → difference = 1

'b' is at index 1 in s and index 0 in t → difference = 1

'c' is at index 2 in both → difference = 0
Total = 1 + 1 + 0 = 2

"""
class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        for i in s:
            res+= abs(s.index(i) - t.index(i))
        return res