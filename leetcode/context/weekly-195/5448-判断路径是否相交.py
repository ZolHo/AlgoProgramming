# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 1:47 下午
# @Author  : ZolHo.github.io
# @FileName: 5448-判断路径是否相交.py

from typing import List


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mp = [(0, 0)]
        dt = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
        mpidx = 0
        for v in path:
            tmp = mp[mpidx]
            ne = (tmp[0] + dt[v][0], tmp[1] + dt[v][1])
            if (ne in mp): return True
            mp.append(ne)
            mpidx += 1
        return False


solu = Solution()
print(solu)
