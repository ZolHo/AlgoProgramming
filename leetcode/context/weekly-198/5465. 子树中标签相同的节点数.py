# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:47 上午
# @Author  : ZolHo.github.io
# @FileName: 5465. 子树中标签相同的节点数.py

from typing import List
from collections import deque
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] *  n
        dt = dict()
        for v in labels:
            if v not in dt.keys():
                dt[v] = []
        dt[labels[0]].append(0)
        tre = dict()
        for a,b in edges:
            if a not in tre.keys():
                tre[a] = [b]
            else :
                tre[a].append(b)
            if b not in tre.keys():
                tre[b] = [a]
            else :
                tre[b].append(a)
        mp = [False] * n
        mp[0] = True
        def dfs(node):
            # print(node, dt[labels[node]])
            for m in dt[labels[node]] :
                ans[m]+=1
            if node not in tre.keys():
                return
            for h in tre[node]:
                if not mp[h] :
                    mp[h] = True
                    dt[labels[h]].append(h)
                    dfs(h)
                    mp[h] = False
                    dt[labels[h]].pop(-1)
        dfs(0)
        return ans




solu = Solution()
print(solu.countSubTrees(
    4
    ,[[0, 2], [0, 3], [1, 2]]
,"aeed"))
