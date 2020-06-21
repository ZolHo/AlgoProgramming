# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 10:06 上午
# @Author  : ZolHo.github.io
# @FileName: 124-二叉树中的最大路径和.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if (not root.left and not root.right ): return root.val
        ans = root.val
        def findmax(node ):
            nonlocal ans
            if (not node): return 0
            l, r = findmax(node.left), findmax(node.right)
            ans = max(l+node.val,r+node.val,l+r+node.val,ans)
            return max(l,r,0)+node.val
        p = findmax(root)
        return max(p,ans)