# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 10:08 上午
# @Author  : ZolHo.github.io
# @FileName: 139-单词拆分.py

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(0,i+1):
                if (dp[j] and s[j:i+1] in wordDict):
                    dp[i+1] = True
        return(dp[len(s)])

solu = Solution()
print(solu.wordBreak("leetcode",  ["leet", "code"]))
