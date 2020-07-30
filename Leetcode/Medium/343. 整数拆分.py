# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 10:47
# @Author  : ZolHo
# @FileName: 343. 整数拆分.py

import math
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
