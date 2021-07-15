from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        anser = 0
        for i,v  in enumerate (chalk):
            if k < v :
                anser = i
                break
            k -= v
        return anser
