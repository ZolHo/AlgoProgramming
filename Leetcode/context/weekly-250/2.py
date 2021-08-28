# @time   :2021/07/18
# @author :ZolHo
# @file   :2.py

from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        lst = 0
        ans = 0
        for i in rungs:
            t = 0
            if i-lst > dist:
                t = (i-lst-1)//dist
                ans+=t
            if t>0:
                lst = lst+t*dist

            lst = max(lst,i)
        return ans