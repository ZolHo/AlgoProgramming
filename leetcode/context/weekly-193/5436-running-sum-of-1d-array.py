# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 12:21 下午
# @Author  : ZolHo
# @FileName: 5436-running-sum-of-1d-array.py

from typing import List
from functools import reduce
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [reduce(lambda x,y : x + y, nums[0:i+1])  for i in range(len(nums))]

solu = Solution()
print(solu.runningSum([1,2,3,4]))
