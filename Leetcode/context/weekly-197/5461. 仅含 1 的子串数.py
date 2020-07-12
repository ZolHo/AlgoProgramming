# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 9:36 上午
# @Author  : ZolHo.github.io
# @FileName: 5461. 仅含 1 的子串数.py

from typing import List
class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        sb = s.split('0')
        for v in sb:
            if v !='' :
                bb = len(v)
                ans += bb*(bb+1)/2
                ans %=1000000007
        return ans
solu = Solution()
print(solu)
