# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 11:24 下午
# @Author  : ZolHo
# @FileName: 2-add-two-numbers.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1, a2, i = 0, 0, 1
        while (l1!=None):
            a1 += i*l1.val
            l1 = l1.next
            i *= 10
        i = 1
        while (l2!=None):
            a2 += i*l2.val
            l2 = l2.next
            i *= 10
        a3 = a1+a2
        l3 = ListNode()
        temp = l3
        while (a3 != 0 ):
            temp.val = a3%10
            a3 //= 10
            if (a3!=0):
                temp.next = ListNode()
                temp = temp.next
        return l3

solu = Solution()
solu.addTwoNumbers()
