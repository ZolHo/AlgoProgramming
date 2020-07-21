# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 11:00 上午
# @Author  : ZolHo.github.io
# @FileName: 4-寻找两个正序数组的中位数.py

'/Applications/IntelliJ IDEA.app/Contents/bin/JetbrainsIdesCrack-4.2-release-sha1-3323d5d0b82e716609808090d3dc7cb3198b8c4b.jar'
from typing import List
from bisect import bisect_left
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenth = len(nums2) + len(nums1)
        flag = lenth % 2 == 0

        def findkth(n1, n2, k) :
            print(n1,n2,k)
            if (len(n1) == 0): return n2[k - 1]
            if (len(n2) == 0): return n1[k - 1]
            if (k==1) : return min(n1[0], n2[0])
            if (len(n1) < len(n2)) : n1, n2 = n2, n1
            t2 = min (k//2, len(n2))
            t1 = k - t2
            print(t1,t2)
            if (n1[t1-1]>n2[t2-1]) : return findkth(n1, n2[t2:], k-t2)
            else: return findkth(n1[t1:],n2, k-t1)

        if (flag):
            center = lenth // 2
            return (findkth(nums2, nums1, center) + findkth(nums2,nums1, center+1))/2
        else:
            center = (lenth + 1) // 2
            return findkth(nums1, nums2,center)

solu = Solution()
print(solu.findMedianSortedArrays([1,2]
,[3,4]))