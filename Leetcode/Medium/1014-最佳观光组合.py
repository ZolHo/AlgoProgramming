# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 10:30 上午
# @Author  : ZolHo.github.io
# @FileName: 1014-最佳观光组合.py

from typing import List
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans, lastmax = 0, A[0]
        for i, v in enumerate(A[1:]):
            lastmax -= 1
            lastmax = max(lastmax,A[i])
            ans = max(ans, lastmax-1+v)
        return ans

solu = Solution()
print()