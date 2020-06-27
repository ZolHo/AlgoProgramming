# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 11:41 下午
# @Author  : ZolHo.github.io
# @FileName: 5433-n 的第 k 个因子.py

from typing import List
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        le = 0
        ansl = []
        for i in range(1,n+1):
            if(n%i==0) :
                le += 1
                ansl.append(i)
        if(k>le) : return -1
        return ansl[k-1]