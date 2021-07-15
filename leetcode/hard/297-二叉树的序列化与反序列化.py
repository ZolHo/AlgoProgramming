# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:34 上午
# @Author  : ZolHo.github.io
# @FileName: 297-二叉树的序列化与反序列化.py

from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        num, data, chir = 0, [], []
        queue = deque()
        if (not root ) : return None
        queue.append(root)
        while (len(queue)) :
            tmp = queue.popleft()
            data.append(tmp.val)
            l , r = '0', '0'
            if(tmp.left) :
                l = '1'
                queue.append(tmp.left)
            if(tmp.right) :
                r = '1'
                queue.append(tmp.right)
            chir.append((l,r))
        s = ''
        s+=str(len(data)) +":" +str(data[0])
        for i in data[1:]:
            s+=","+ str(i)
        s+=":"+ chir[0][0]+chir[0][1]
        for i in chir[1:]:
            s+=","+ i[0] +i[1]
        return s

    def deserialize(self, data):
        if (not data) : return None
        n, das, sits = data.split(':')
        da,sit = das.split(','), sits.split(',')
        root = TreeNode()
        queue = deque()
        queue.append(root)
        for i in range(int(n)):
            tmp = queue.popleft()
            tmp.val = da[i]
            if (sit[i][0]=='1') :
                left = TreeNode()
                tmp.left = left
                queue.append(left)
            if (sit[i][1] == '1'):
                right = TreeNode()
                tmp.right = right
                queue.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))