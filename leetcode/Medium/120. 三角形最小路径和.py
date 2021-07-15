# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 10:52 上午
# @Author  : ZolHo.github.io
# @FileName: 120. 三角形最小路径和.py

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        fuzhu = [v for v in triangle[-1]]
        for i in range(len(triangle)-1)[::-1]:
            for j in range(len(triangle[i])):
                fuzhu[j] = min(fuzhu[j],fuzhu[j+1]) + triangle[i][j]
        return fuzhu[0]


solu = Solution()
print(solu)
