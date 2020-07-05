# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:24 上午
# @Author  : ZolHo.github.io
# @FileName: 5452-判断能否形成等差数列.py

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        cha = arr[1] - arr[0]
        lst = arr[0]
        for v in arr[1:]:
            if (v-lst!=cha ) :  return False
            lst = v
        return True
solu = Solution()
print(solu)
