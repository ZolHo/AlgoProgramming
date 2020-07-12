# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 7:47 下午
# @Author  : ZolHo.github.io
# @FileName: 617. 合并二叉树.py

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2 : return t1 if not t2 else t2
        newnode = TreeNode(t1.val+t2.val)
        def digui (node1, node2, newnode) :
            if node1.left and node2.left :
                newnode.left = TreeNode(node1.left.val+ node2.left.val)
                digui(node1.left, node2.left, newnode.left)
            elif node1.left and not node2.left :
                newnode.left = node1.left
            else : newnode.left = node2.left
            if node1.right and node2.right :
                newnode.right = TreeNode(node1.right.val+ node2.right.val)
                digui(node1.right, node2.right, newnode.right)
            elif node1.right and not node2.right :
                newnode.right = node1.right
            else : newnode.right = node2.right
        digui(t1,t2,newnode)
        return newnode
solu = Solution()
print(solu.mergeTrees())
