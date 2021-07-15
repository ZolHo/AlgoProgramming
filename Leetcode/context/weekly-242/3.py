class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False for i in range(len(s))]
        dp[0] = True
        last = 0
        for i in range(len(s)) :
            if dp[i] == True :
                for j in range(max(i+minJump, last), min(i+maxJump, len(s)-1)+1) :
                    if s[j] == '0' :
                        dp[j] = True
                last = j
        return dp[-1]
