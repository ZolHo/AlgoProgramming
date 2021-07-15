# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 10:30 上午
# @Author  : ZolHo.github.io
# @FileName: 337. 打家劫舍 III


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def digui (root) :
            if not root : return [0,0]
            lt, rt = digui(root.left), digui(root.right)
            return root.val + lt[1] + rt[1], max(lt)+max(rt)
        return max(digui(root))



solu = Solution()
print(solu.rob())