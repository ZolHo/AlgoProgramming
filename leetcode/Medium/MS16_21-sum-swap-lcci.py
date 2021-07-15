# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 2:48 下午
# @Author  : ZolHo
# @FileName: MS16_21-sum-swap-lcci.py

from typing import List

class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        a1_sum, a2_sum, a2_dict = 0, 0, {}
        for i in array1:
            a1_sum+=i
        for i in array2:
            a2_sum+=i
            a2_dict[i] = 1
        two_sum = a1_sum+a2_sum
        if (two_sum%2!=0):
            return []
        avle = int(two_sum/2)
        for i in set(array1):
            if (avle-a1_sum+i in a2_dict.keys()):
                return [i,avle-a1_sum+i]
        return []

solu = Solution()
print(solu.findSwapValues([4, 1, 2, 1, 1, 2],[3,6,3,3]))