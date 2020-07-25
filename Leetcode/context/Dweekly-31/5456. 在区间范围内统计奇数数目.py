# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:12 下午
# @Author  : ZolHo.github.io
# @FileName: 5456. 在区间范围内统计奇数数目


from typing import List
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        if high-low ==1:return 1
        if (high - low )%2==0:
            if low %2==0:
                ans = (high-low)//2
            else:
                ans = (high-low)//2+1
        else :
            ans = (high-low)//2+1
        return ans
solu = Solution()
print(solu)