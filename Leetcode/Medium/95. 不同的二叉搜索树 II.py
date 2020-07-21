# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:24 AM
# @Author  : ZolHo.github.io
# @FileName: 95. 不同的二叉搜索树 II.py

# 我的递归有问题，找不出来，懒的搞，copy别人的了

from typing import List
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dct = {}

        def left_right(left: int, right: int) -> List[TreeNode]:
            if left > right:
                return [None]
            if (left, right) in dct:
                return dct[(left, right)]
            ret = []
            for i in range(left, right+1):
                left_lst = left_right(left, i-1)
                right_lst = left_right(i+1, right)
                for L in left_lst:
                    for R in right_lst:
                        app_Tree = TreeNode(i)
                        app_Tree.left = L
                        app_Tree.right = R
                        ret.append(app_Tree)
            dct[(left, right)] = ret
            return ret

        left_right(1, n)
        return left_right(1, n)

# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/python3-xiang-xi-di-gui-by-ting-ting-28/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

solu = Solution()
print(solu.generateTrees(0))