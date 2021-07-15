# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 12:26 上午
# @Author  : ZolHo.github.io
# @FileName: 63-不同路径 II.py

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1
        if (len(obstacleGrid) == 1): return dp[0][len(obstacleGrid[0]) - 1]
        if (len(obstacleGrid[0]) == 1): return dp[len(obstacleGrid) - 1][0]
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[i][j]


solu = Solution()
print(solu)
