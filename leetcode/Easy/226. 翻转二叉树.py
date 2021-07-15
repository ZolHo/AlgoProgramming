# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 7:58 下午
# @Author  : ZolHo.github.io
# @FileName: 226. 翻转二叉树.py

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def digui ( node ):
            if not node : return
            node.left , node.right = node.right, node.left
            digui(node.left)
            digui(node.right)
        digui(root)
        return root
solu = Solution()
print(solu)
