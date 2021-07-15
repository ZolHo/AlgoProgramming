# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 12:14 下午
# @Author  : ZolHo.github.io
# @FileName: 1300-转变数组后最接近目标值的数组和.py

from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr = sorted(arr)
        left, right = target//len(arr)-1, arr[-1]
        ans = right
        def outsum(a, v):
            s = 0
            for i in a:
                if (i > v):
                    s += v
                else:
                    s += i
            return abs(s - target)

        minv = abs(sum(arr) - target)
        while (left < right):
            mid = (left + right) // 2
            leftv = outsum(arr,left)
            rightv = outsum(arr,right)
            midv = outsum(arr,mid)
            newmin = min(minv, leftv, rightv,midv)
            if (newmin == leftv):
                if (newmin==minv):
                    ans = min (ans, left)
                else:
                    ans = left
            if (newmin == rightv):
                if (newmin == minv):
                    ans = min(ans, right)
                else:
                    ans = right
            if (newmin == midv):
                if (newmin == minv):
                    ans = min(ans, mid)
                else:
                    ans = mid
            minv = newmin
            if (leftv > rightv):
                left = mid+1
            else:
                right = mid
        return ans


solu = Solution()
print(solu.findBestValue([4,9,3]
,10))