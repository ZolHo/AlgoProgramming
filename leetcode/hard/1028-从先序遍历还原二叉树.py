# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 9:43 上午
# @Author  : ZolHo.github.io
# @FileName: 1028-从先序遍历还原二叉树.py

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if (len(S)<=2) : return TreeNode(S[0])
        name = S.split('-')
        while '' in name : name.remove('')
        cha, gether, tongji, j = S[2], 0, [(name[0],0)], 1
        for i in range(1,len(S)):
            if (S[i] in '1234567890') :
                if (gether!=0):
                    tongji.append((name[j],gether))
                    j += 1
                    gether = 0
            else: gether += 1
        stack = []
        print(tongji)
        root = TreeNode(name[0])
        stack.append((root, tongji[0][1]))
        for v in tongji[1:]:
            while( stack[-1][1]!=v[1]-1) :
                stack.pop()
            tmp = TreeNode(v[0])
            if (not stack[-1][0].left): stack[-1][0].left = tmp
            else : stack[-1][0].right = tmp
            stack.append((tmp,v[1]))
        return root

solu = Solution()
print(solu.recoverFromPreorder("10-7--8"))