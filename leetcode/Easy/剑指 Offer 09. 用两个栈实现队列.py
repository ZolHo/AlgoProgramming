# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 11:33 上午
# @Author  : ZolHo.github.io
# @FileName: 剑指 Offer 09. 用两个栈实现队列.py

from typing import List
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if(len(self.stack1)==0 and len(self.stack2)==0): return -1
        if(len(self.stack2)>0) :
            ans = self.stack2[len(self.stack2)-1]
            self.stack2 = self.stack2[0:len(self.stack2)-1]
            return ans
        for v in self.stack1[::-1]:
            self.stack2.append(v)
        ans = self.stack2[len(self.stack2)-1]
        self.stack2 = self.stack2[:len(self.stack2)-1]
        self.stack1 = []
        return ans



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()