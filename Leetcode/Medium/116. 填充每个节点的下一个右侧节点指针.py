# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 10:05 上午
# @Author  : ZolHo.github.io
# @FileName: 116. 填充每个节点的下一个右侧节点指针


from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        temp1, temp2 = None, None

        def digui(node, k):
            if not node or not node.left: return
            temp1, temp2 = node.right, node.left
            temp2.next = temp1
            while temp1.left:
                temp1 = temp1.left
                temp2 = temp2.right
                temp2.next = temp1

            if node.left:
                digui(node.left, 1)
                digui(node.right, 1)

        digui(root, 1)
        return root



solu = Solution()
print(solu)