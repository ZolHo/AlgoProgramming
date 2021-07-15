# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 9:30 下午
# @Author  : ZolHo.github.io
# @FileName: 1483-树节点的第K个祖先.py

from typing import List
from math import pow
from math import log2
class TreeAncestor:
    # n : int
    # parant : List[int]
    # beizeng = []

    def __init__(self, n: int, parent: List[int]):
        self.n, self.parant = n, parent
        self.beizeng = []
        self.beizeng.append(parent)
        for i in range(1,int(log2(len(parent))+1)):
            temp = [-2 for x in range(len(parent))]
            for j in range(len(parent))[::-1]:
                if (self.beizeng[i-1][j] > 0) :
                    temp[j] = self.beizeng[i-1][self.beizeng[i-1][j]]
                else : continue
            self.beizeng.append(temp)
        print(self.beizeng)

    def getKthAncestor(self, node: int, k: int) -> int:
        step = int(log2(k))
        sxd = k - int(pow(2, step))
        if(step>=len(self.beizeng)):return -1
        # print(step,sxd)
        while (k>0 and step >= 0):
            tmp = self.beizeng[step][node]
            if (tmp<0 ) : return -1
            elif(sxd==0): return tmp
            node = tmp
            step = int(log2(sxd))
            k = sxd
            sxd = sxd - int(pow(2,step))




obj = TreeAncestor(10,[-1,0,0,1,2,0,1,3,6,1])
print(obj.getKthAncestor(4,2))
print(obj.getKthAncestor(3,1))
# print(obj.getKthAncestor(6,3))
# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
