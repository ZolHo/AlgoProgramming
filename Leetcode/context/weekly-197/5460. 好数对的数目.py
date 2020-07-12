# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 9:36 上午
# @Author  : ZolHo.github.io
# @FileName: 5460. 好数对的数目.py

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]: ans+=1

        return ans

solu = Solution()
print(solu)
