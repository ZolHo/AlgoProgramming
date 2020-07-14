# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 12:14 上午
# @Author  : ZolHo.github.io
# @FileName: 96. 不同的二叉搜索树.py

from typing import List
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+4)
        dp[1],dp[2],dp[3] = 1,2,5
        for i in range(4,n+1):
            dp[i] = 2*dp[i-1]
            for j in range(1,i-1):
                dp[i]+=dp[j] *dp[i-1-j]
        return dp[n]

solu = Solution()
print(solu)
