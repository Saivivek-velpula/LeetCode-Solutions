"""Problem: 762. Prime Number of Set Bits in Binary Representation
Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

Level: Easy

Description:
You are given two integers left and right.

For every integer x in the range [left, right] (inclusive), consider its binary representation and count the number of set bits (i.e., the number of 1s in its binary form).

Your task is to return the total number of integers in the given range whose count of set bits is a prime number.

A prime number is a number greater than 1 that has exactly two positive divisors: 1 and itself.

Example 1:

Input:

left = 6
right = 10

Output:

4

Explanation:

Numbers in range: 6, 7, 8, 9, 10

Binary representations and set bits:

6 → 110 → 2 set bits (prime)

7 → 111 → 3 set bits (prime)

8 → 1000 → 1 set bit (not prime)

9 → 1001 → 2 set bits (prime)

10 → 1010 → 2 set bits (prime)

There are 4 numbers with a prime number of set bits → return 4.
"""
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def primeno(n):
            c=0
            if n<2:
                return False
            for i in range(2,n):
                if n%i==0:
                    return False    
            return True 
        c =0
        for i in range(left,right+1):
            bit = bin(i)[2:]
            count = 0
            for i in bit:
                if i == '1':
                    count+=1
            p = primeno(count)
            if p== True:
                c+=1
        return c