# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 2:26 下午
# @Author  : ZolHo.github.io
# @FileName: 174. 地下城游戏.py

from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        dp[-1][-1] = dungeon[-1][-1] if dungeon[-1][-1] < 0 else 0

        for i in range(len(dungeon[0])-1)[::-1]:
            tmp = dp[-1][i+1] + dungeon[-1][i]
            if tmp >= 0: dp[-1][i] = 0
            else : dp[-1][i] = tmp

        for i in range(len(dungeon)-1)[::-1]:
            tmp = dp[i+1][-1] + dungeon[i][-1]
            if tmp >= 0:dp[i][-1] = 0
            else:dp[i][-1] = tmp

        for i in range(len(dungeon)-1)[::-1] :
            for j in range(len(dungeon[0])-1)[::-1]:
                mx = max(dp[i+1][j], dp[i][j+1])
                mx+=dungeon[i][j]
                if mx >= 0: dp[i][j] = 0
                else : dp[i][j] = mx
        # print (dp)
        if dp[0][0] > 0 : return 1
        else: return abs(dp[0][0]) +1

solu = Solution()
print(solu)
