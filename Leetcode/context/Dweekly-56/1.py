from typing import List

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1) :
            for j in range(1, n+1):
                t = i**2 + j**2
                t_s = t**0.5
                if int(t_s) **2 == t and t_s <= n :
                    ans+=1
        return ans
