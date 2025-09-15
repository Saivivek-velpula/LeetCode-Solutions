"""
Problem: 1945. Sum of Digits of String After Convert
Link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

Level: Easy

Description:
You are given a string s consisting of lowercase English letters, and an integer k. First, convert each letter in s to its position in the alphabet ('a' -> 1, 'b' -> 2, ..., 'z' -> 26) and concatenate these numbers to form a new string of digits. Then, repeatedly replace the string with the sum of its digits (as a decimal integer converted back to a string) exactly k times. Return the resulting string after performing the operation k times.

Example 1:
Input: s = "iiii", k = 1
Output: "36"
Explanation: 'i' -> 9 so concatenation -> "9999". Sum of digits = 9+9+9+9 = 36. After 1 operation result is "36".

Example 2:
Input: s = "leetcode", k = 2
Output: "6"
Explanation:

Convert: l(12) e(5) e(5) t(20) c(3) o(15) d(4) e(5) -> concatenation "12552031545".

1st sum: 1+2+5+5+2+0+3+1+5+4+5 = 33 -> "33".

2nd sum: 3+3 = 6 -> "6".

Constraints:

1 <= s.length <= 100

1 <= k <= 10

s consists only of lowercase English letters.
"""
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        su =""
        for i in s:
            su = su+ str(ord(i)-96)
        n = int(su)
        while k>0:
            val =0
            while n>0:
                val += n%10
                n = n//10
            n = val
            k-=1     
        return n