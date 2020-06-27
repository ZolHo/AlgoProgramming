# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 11:41 下午
# @Author  : ZolHo.github.io
# @FileName: 5434-删掉一个元素以后全为 1 的最长子数组.py

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        flag = True
        ct = 0
        ct2 = 0
        for i,v  in enumerate(nums):
            if (v==1) : ct+=1
            else :
                flag = False
                for j in nums[i+1:]:
                    if(j==1): ct2+=1
                    else:break
                ans = max(ans, ct+ct2)
                ct = 0
                ct2 = 0
        if(flag) : return len(nums)-1
        return ans