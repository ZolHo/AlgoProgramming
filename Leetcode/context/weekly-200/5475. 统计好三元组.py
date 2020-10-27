# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 11:42 上午
# @Author  : ZolHo.github.io
# @FileName: 5475. 统计好三元组


from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        l = len(arr)
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):

                    ii, ij, ik = arr[i], arr[j], arr[k]
                    if abs(ii - ij) <= a and abs(ij - ik) <= b and abs(ii - ik) <= c:
                        ans += 1
        return ans
solu = Solution()
print(solu)