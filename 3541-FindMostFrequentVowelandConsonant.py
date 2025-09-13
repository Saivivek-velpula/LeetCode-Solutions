"""
Problem: 3541. Find Most Frequent Vowel and Consonant
Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
 
LeetCode

Level: Easy

Description:
You are given a string s with only lowercase English letters ('a'-'z').

Find which vowel (one of 'a', 'e', 'i', 'o', 'u') appears most frequently in s, and also which consonant (any letter not a vowel) appears most frequently in s.

Return the sum of the frequency of the most frequent vowel and the frequency of the most frequent consonant.

If there are no vowels in the string, treat the vowel frequency as 0.
If there are no consonants in the string, treat the consonant frequency as 0.

Example:

Input: s = "successes"  
Output: 6


Explanation:

Vowels in "successes": 'u' appears 1, 'e' appears 2 → the most frequent vowel has frequency 2

Consonants: 's' appears 4, 'c' appears 2, etc. → the most frequent consonant has frequency 4

Sum = 2 + 4 = 6

"""

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1 = {"a":0,"e":0,"i":0,"o":0,"u":0}
        d2 = {}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                if i in d2:
                    d2[i]+=1
                else:
                    d2[i]=1
        m1 = 0
        for i in d1:
            if d1[i]>m1:
                m1=d1[i]
        m2 = 0
        for i in d2:
            if d2[i]>m2:
                m2 =d2[i]
        return m1+m2