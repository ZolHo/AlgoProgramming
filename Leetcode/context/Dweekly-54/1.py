from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flag = True
        for i in range(left,right+1) :
            t = False
            for j in ranges :
                if i >= j[0] and i <= j[1] :
                    t = True
                    break
            if not t :
                flag = False
                break
        return flag