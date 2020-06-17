# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 11:00 上午
# @Author  : ZolHo.github.io
# @FileName: 4-寻找两个正序数组的中位数.py

from typing import List
from bisect import bisect_left
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lo, hi = min(nums2[0], nums1[0]), max(nums1[-1], nums2[-1])
        lenth = len(nums2) + len(nums1)
        flag = lenth % 2 == 0
        if (flag):
            center = lenth // 2 - 1
        else:
            center = (lenth - 1) // 2
        while (hi >= lo):
            mid = (hi + lo) // 2
            site1, site2 = bisect_left(nums1, mid), bisect_left(nums2, mid)
            print(lo, hi, mid,site1,site2,center)
            if (site1 + site2 == center):
                if (site1 >= len(nums1)): return nums2[site2]
                if (site2 >= len(nums2)): return nums2[site2]
                return (nums1[site1] + nums2[site2]) / 2 if (flag) else min(nums1[site1], nums2[site2])
            if (site1 + site2 > center):
                hi = mid
            else:
                lo = mid + 1

solu = Solution()
print(solu.findMedianSortedArrays([1,2,3,3]
,[3,4,5,6,8,40]))