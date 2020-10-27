# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 8:59 下午
# @Author  : ZolHo.github.io
# @FileName: 114. 二叉树展开为链表


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        lastone = TreeNode()
        def chuli (root:TreeNode ) :
            nonlocal lastone
            lt, rt = root.left, root.right
            if lt and rt:
                chuli(lt)
                root.right = lt
                root.left = None
                lastone.right = rt
                chuli(rt)
            if lt and not rt:
                chuli(lt)
                root.right = lt
                root.left = None
            if not lt and rt:
                chuli(rt)
            if not lt and not rt:
                lastone = root
        chuli(root)
solu = Solution()
print(solu)