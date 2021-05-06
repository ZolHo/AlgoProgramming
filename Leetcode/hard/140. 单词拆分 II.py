from typing import List



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def wordBreak(s, wordDict):
            dp = [False for i in range(len(s) + 1)]
            dp[0] = True
            for i in range(len(s)):
                for j in range(0, i + 1):
                    if (dp[j] and s[j:i + 1] in wordDict):
                        dp[i + 1] = True
            return (dp)
        sdict = {}
        wset = set(wordDict)
        def digui(s) :
            rs = []
            if s in sdict:
                return sdict[s]
            if s in wset:
                rs = [[s]]
            dp = wordBreak(s, wordDict)
            if not dp[-1] :
                return []

            for i in range(len(s)+1) :
                if s[:i] in wordDict :
                    temp = digui(s[i:])
                    for t in temp:
                        rs.append([s[:i]] + t)
            sdict[s] = rs
            return rs
        return [" ".join(i) for i in digui(s)]