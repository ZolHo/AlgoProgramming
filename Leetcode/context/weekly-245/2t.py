from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lo, hi, mid = 0, len(removable), len(removable)//2
        while lo < hi :
            isre = [False for _ in range(len(s))]
            for i in range(mid+1) :
                isre[removable[i]] = True
            flag = False
            idx = 0
            for i in range(len(s)) :
                if p[idx]==s[i] and isre[i] == False:
                    idx+=1
                    if idx == len(p):
                        flag = True
                        break
            if flag: lo = mid+1
            else : hi = mid
            mid = (lo+hi)//2
        return mid


