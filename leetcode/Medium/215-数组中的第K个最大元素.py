# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 10:46 上午
# @Author  : ZolHo.github.io
# @FileName: 215-数组中的第K个最大元素.py

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse=True)[k-1]
solu = Solution()
print(solu)
