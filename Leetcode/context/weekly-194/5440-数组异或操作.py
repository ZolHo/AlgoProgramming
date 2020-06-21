# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 12:28 下午
# @Author  : ZolHo.github.io
# @FileName: 5440-数组异或操作.py

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        ans = nums[0]
        for v in nums[1:]:
            ans ^= v
        return ans