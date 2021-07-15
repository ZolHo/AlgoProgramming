from typing import List
from functools import reduce
import operator

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mo = 1e9+7
        nums.sort()
        t0 = [1 for i in range(len(nums)-1)]
        for i in range( len(t0)) :
            t0[i] = nums[i+1] / nums[i]
        t1 = [t0[0]]
        last = 0
        anser = 0
        for i in range(1, len(t0)):
            now = len(t1)
            for j in range(last, now) :
                t1.append(t0[i] * t1[j])
            t1.append(t0[i])
            last = now
        for i in range(len(t1)) :
            anser += int (t1[i])

        return int ((anser+len(nums))%mo)

