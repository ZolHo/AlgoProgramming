# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 12:13 下午
# @Author  : ZolHo.github.io
# @FileName: 剑指 Offer 07. 重建二叉树.py

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        dt_zhong, dt_qian = {}, {}
        for i,v in enumerate(inorder):
            dt_zhong[v] = i
        for i, v in enumerate(preorder):
            dt_qian[v] = i
        root = TreeNode(preorder[0])

        def dfs (father, l,r ,  is_l):
            if l>=r  : return
            if r-l==1 :
                if is_l: father.left = TreeNode(inorder[l])
                else: father.right = TreeNode(inorder[l])
            minqian = n
            for i in range(l,r):
                minqian = min(minqian, dt_qian[inorder[i]])
            va = preorder[minqian]
            tmp = TreeNode(va)
            if is_l:
                father.left = tmp
            else:
                father.right = tmp

            dfs(tmp, l, dt_zhong[va], True)
            dfs(tmp, dt_zhong[va]+1,r,  False)
        dfs(root, 0, dt_zhong[preorder[0]],  True)
        dfs(root, dt_zhong[preorder[0]]+1, n,  False)
        return root


solu = Solution()
print(solu.buildTree([3,9,20,15,7]
,[9,3,15,20,7]))
