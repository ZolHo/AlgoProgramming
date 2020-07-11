# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 12:29 下午
# @Author  : ZolHo.github.io
# @FileName: 315. 计算右侧小于当前元素的个数.py

from typing import List
from collections import Counter
class bitTree():
    def __init__(self, arr) :
        self.n = len(arr)
        n = self.n
        self.a = [0 for i in range(n+1)]
        for i in range(n):
            self.update(i, arr[i])

    def lowbit(self, i) :
        return i & -i;

    def update (self, i,  val) :
        i = i+1
        while i <= self.n :
            self.a[i] += val;
            i += self.lowbit(i);

    def sum (self, i) :
        i = i+1
        ret = 0;
        while i > 0 :
            ret += self.a[i];
            i -= self.lowbit(i);
        return ret;

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        ky, dctsite, ans, sm = [], {}, [],[]
        for v in ct.keys():
            ky.append(v)
        ky.sort()
        for i,v in enumerate(ky):
            dctsite[v] = i
            sm.append(ct[v])
        sm = bitTree(sm)
        print(dctsite,ky)
        for v in nums:

            if dctsite[v] == 0 :
                ans.append(0)
                sm.update(dctsite[v], -1)
                continue
            ans.append(sm.sum(dctsite[v]-1))
            sm.update(dctsite[v], -1)

        return ans

solu = Solution()
print(solu.countSmaller([-1,0]))
