# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 10:27 下午
# @Author  : ZolHo.github.io
# @FileName: 5445. 子数组和排序后的区间和.py

from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        qzh = [nums[0]] * len(nums)
        for i in range(1,len(nums)):
            qzh[i] = nums[i]+qzh[i-1]
        oth = qzh.copy()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                qzh[j] -= qzh[i]
                oth.append(qzh[j])
        oth.sort()

        ans = 0
        for i in range(left-1,right):

            ans += oth[i]
            ans%=1000000007
        return ans


solu = Solution()
print(solu.rangeSum([1,2,3,4]
,4
,1
,5))
