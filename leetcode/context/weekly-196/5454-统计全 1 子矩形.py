# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:24 上午
# @Author  : ZolHo.github.io
# @FileName: 5454-统计全 1 子矩形.py

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        qzh = [[0 for j in range(len(mat[0])+1)] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                qzh[i][j] = mat[i][j] + qzh[i][j-1]

        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1) :





solu = Solution()
print(solu)
