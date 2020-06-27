# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 9:46 上午
# @Author  : ZolHo.github.io
# @FileName: 41-缺失的第一个正数.py

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if(len(nums)==0): return 1
        tb = [0 for i in range (len(nums)+1)]
        for i in nums:
            if(i>0 and i<=len(nums)) :
                tb[i] = 1
        for i in range(1,len(nums)+1):
            if(tb[i]==0) : return i
        return i+1


solu = Solution()
print(solu)
