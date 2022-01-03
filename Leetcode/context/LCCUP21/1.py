# @time   :2021/09/11
# @author :ZolHo
# @file   :1.py

from typing import List
from collections import Counter

class Solution:
    def minimumSwitchingTimes(self, source: List[List[int]], target: List[List[int]]) -> int:
        a = [i for k in source for i in k]
        b = [i for k in target for i in k]
        ac = Counter(a)
        bc = Counter(b)
        ans = 0
        for i in bc :
            if i in ac :
                if ac[i] < bc[i] :
                    ans += bc[i] - ac[i]
            else :
                ans += bc[i]
        return ans


