from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def ziji(items):
            N = len(items)
            re = []
            for i in range(2 ** N):
                combo = []
                for j in range(N):
                    if (i >> j) % 2:
                        combo.append(items[j])
                re.append(combo)
            return re

        zj  = ziji(nums)
        anser = 0
        for i in zj :
            t = 0
            for j in i:
                t^=j
            anser+=t
        return anser