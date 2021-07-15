# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:12 下午
# @Author  : ZolHo.github.io
# @FileName: 5458. 字符串的好分割数目


from typing import List
from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        mm = Counter(s)
        left = {}
        ans = 0
        l,r = 0, mm.__len__()
        for i in s:
            mm[i] -= 1
            if i not in left:
                left[i] = 1
            else:
                left[i]+=1
            if mm[i] == 0:
                mm.pop(i)
            if mm.__len__()==left.__len__():
                ans+=1
        return ans
solu = Solution()
print(solu)