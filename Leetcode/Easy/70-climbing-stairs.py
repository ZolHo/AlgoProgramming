# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:49 上午
# @Author  : ZolHo
# @FileName: 70-climbing-stairs.py

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n)]
        if (n>=2):
            dp[1] = 2
        dp[0] = 1
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n-1]

solu = Solution()
print(solu.climbStairs(n=3))