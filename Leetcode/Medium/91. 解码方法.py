from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] =='0' :
            return 0
        k = set([str(i) for i in range(1,27)])
        dp = [0 for i in range(len(s)+1)]
        dp[1] = 1
        if s[:2] in k :
            dp[0] = 1
        for i in range (1, len(s)):
            if s[i] == '0' and s[i-1:i+1] not in k :
                return 0
            tp1, tp2 = 0, 0
            if s[i] in k :
                tp1 = dp[i]
            if s[i-1:i+1] in k:
                tp2 = dp[i-1]
            dp[i+1] = tp1+tp2
        return dp[-1]
