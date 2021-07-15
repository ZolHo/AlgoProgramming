# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:47 上午
# @Author  : ZolHo.github.io
# @FileName: 5464. 换酒问题.py

from typing import List
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        ans += numBottles
        while numBottles >= numExchange:
            yu = numBottles % numExchange
            ans += numBottles//numExchange
            numBottles = yu + numBottles//numExchange

        return ans
solu = Solution()
print(solu.numWaterBottles(15,4))
