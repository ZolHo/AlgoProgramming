# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 10:27 下午
# @Author  : ZolHo.github.io
# @FileName: 5446. 三次操作后最大值与最小值的最小差.py

from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4 : return 0
        nums.sort()
        k = len(nums) - 4
        fuzhu = []
        for i in range(k,len(nums)):
            fuzhu.append(abs(nums[i]-nums[i-k]))
            print(fuzhu)
        print(fuzhu)
        fuzhu.sort()
        return fuzhu[0]


solu = Solution()
print(solu.minDifference([20,66,68,57,45,18,42,34,37,58]))
