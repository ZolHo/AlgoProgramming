# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 8:00 下午
# @Author  : ZolHo.github.io
# @FileName: 209-长度最小的子数组.py

from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        ans = len(nums)+1
        i,j,sm = 0,0, 0
        while j < len(nums):
            sm+=nums[j]
            while sm >= s:
                print(i,j,sm)
                sm -= nums[i]
                ans = min(ans, j-i+1)
                i += 1
            j+=1
        return ans if ans<=len(nums) else 0
solu = Solution()
print(solu)
