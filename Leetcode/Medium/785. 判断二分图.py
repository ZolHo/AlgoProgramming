# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 4:51 下午
# @Author  : ZolHo.github.io
# @FileName: 785. 判断二分图.py

from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        mp = [-1] * len(graph)
        for i in range(len(graph)):
            if mp[i] != -1: continue
            dque = deque()
            dque.append(i)
            mp[i] = 1
            while len(dque) > 0:
                tmp = dque.pop()
                biaoji = mp[tmp]
                for j in graph[tmp]:
                    if mp[j] == -1:
                        mp[j] = 1 - biaoji
                        dque.appendleft(j)
                    elif mp[j] != 1 - biaoji:
                        return False

        return True

solu = Solution()
print(solu.isBipartite([[1,3],[0,2],[1,3],[0,2]]))
