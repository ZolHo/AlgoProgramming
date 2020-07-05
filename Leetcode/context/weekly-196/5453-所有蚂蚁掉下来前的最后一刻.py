# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:24 上午
# @Author  : ZolHo.github.io
# @FileName: 5453-所有蚂蚁掉下来前的最后一刻.py

from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        rt = [n-v for v in right]
        return max(rt+left)

solu = Solution()
print(solu)
