# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 10:59 上午
# @Author  : ZolHo.github.io
# @FileName: 112. 路径总和.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs (nd, father, sum) :
            if not nd: return False
            nd.val += father
            if (not nd.left and not nd.right and nd.val == sum) :
                return True
            l,r = False, False
            if nd.left: l =  dfs(nd.left, nd.val, sum)
            if nd.right : r = dfs(nd.right, nd.val, sum)
            if l or r : return True
            else : return False
        return dfs(root,0,sum)