# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 10:49 上午
# @Author  : ZolHo.github.io
# @FileName: 309. 最佳买卖股票时机含冷冻期.py

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1 : return 0
        dp = [[0,0,0]  for i in range(len(prices)+1) ]
        dp[0][0] = - prices[0]
        ans = 0
        for i,v in enumerate(prices[1:]):
            i+=1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i]);
            dp[i][1] = dp[i - 1][0] + prices[i];
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2]);
        ans = 0
        for v in dp:
            ans = max(ans,max(v))
        return ans



solu = Solution()
print(solu)
