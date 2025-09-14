"""
Problem: 2520. Count the Digits That Divide a Number

Link: LeetCode - Count the Digits That Divide a Number

Level: Easy

Description:

Given an integer num, count how many digits in num divide num.

Ignore any digit equal to 0 since division by zero is not allowed.

A digit divides num if num % digit == 0.

Return the count of such digits.

Example 1:

Input:

num = 121


Output:

2


Explanation:

Digits = [1, 2, 1]

121 % 1 == 0 → valid

121 % 2 == 1 → not valid

121 % 1 == 0 → valid

Count = 2
"""
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        n=num
        while n>0:
            r = n%10
            if num%r==0:
                c+=1
            n=n//10
        return c