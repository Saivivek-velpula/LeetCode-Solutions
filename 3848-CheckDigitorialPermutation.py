"""Problem: 3848. Check Digitorial Permutation
Link: https://leetcode.com/problems/check-digitorial-permutation/

Level: Easy

Description:
You are given a positive integer n.

A number is called a digitorial permutation if:

Take each digit of n.

Compute the factorial of each digit.

Form a new number by arranging (permuting) those factorial values.

The newly formed number equals the original number n.

Your task is to return true if n is a digitorial permutation. Otherwise, return false.

Example 1:

Input:

n = 145

Output:

true

Explanation:

Digits of 145 → 1, 4, 5

Factorials:

1! = 1

4! = 24

5! = 120

Using these factorial values, we can arrange them to form 145.
So return true.
"""
class Solution(object):
    def isDigitorialPermutation(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        su = 0
        while n>0:
            r = n%10
            n = n//10
            fact = 1
            for i in range(1,r+1):
                fact*=i
            su+=fact
        d = {}
        s1 = str(num)
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s2 = str(su)
        for i in s2:
            if i in d:
                d[i]-=1
            else:
                return False
        for i in d:
            if d[i]!=0:
                return False
        return True