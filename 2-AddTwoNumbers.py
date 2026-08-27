"""
Problem: 2. Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/

Level: Medium

Description:

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains a single digit.

Your task is to add the two numbers and return the result as a linked list, also represented in reverse order.

You may assume that the numbers do not contain leading zeros, except for the number 0 itself.

Example:

Input:

l1 = [2,4,3]
l2 = [5,6,4]

Output:

[7,0,8]

Explanation:

The linked lists represent:

l1 → 342
l2 → 465

Adding them:

342 + 465 = 807

Since the result is stored in reverse order:

807 → [7,0,8]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = []
        temp = l1
        while temp!=None:
            list1.append(temp.val)
            temp=temp.next

        list2 = []
        temp = l2
        while temp!=None:
            list2.append(temp.val)
            temp=temp.next
        
        list1.reverse()
        list2.reverse()

        n1 = 0
        for i in list1:
            n1 = n1*10 + i

        n2 = 0
        for i in list2:
            n2 = n2*10 + i

        n = n1+n2
        L= []
        while n>0:
            r = n%10
            n=n//10
            L.append(r)
        if len(L)==0:
            return l1
        head = ListNode(L[0])
        head.next=None
        temp = head
        for i in L[1:]:
            node = ListNode(i)
            temp.next = node
            temp = temp.next

        return head