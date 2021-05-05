from typing import List
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        lst = list(set(nums))
        lst.sort()
        c = Counter(nums)
        dp = [0 for i in range(1+len(lst))]
        dp[1] = c[lst[0]] * lst[0]
        if len(lst) == 1:
            return dp[1]
        for i in range(2, len(lst)+1) :
            if lst[i-1] - lst[i-2] == 1:
                dp[i] = max(dp[i-1], dp[i-2] + lst[i-1] * c[lst[i-1]])
            else :
                dp[i] = dp[i-1] + lst[i-1] * c[lst[i-1]]
        return dp[-1]
