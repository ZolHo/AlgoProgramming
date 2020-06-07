# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 10:24 上午
# @Author  : ZolHo
# @FileName: LCP_06-na-ying-bi.py

class Solution:
    def minCount(self, coins) -> int:
        ans = 0
        for x in coins:
            ans += x//2 + x%2
        return ans
