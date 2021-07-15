# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 10:20 下午
# @Author  : ZolHo.github.io
# @FileName: 32-最长有效括号.py

from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        lst = s[0]
        dp = [0 for i in range(len(s)+1)]
        for i,v in enumerate(s[1:]):
            i+=1
            if v==')':
                if lst=='(':
                    dp[i] = dp[i-2]+2
                else:
                    di = i-1-dp[i-1]
                    if di>=0 and s[di]=='(' :
                        dp[i] = dp[i-1] + 2
                        if di>0:dp[i]+=dp[di-1]

            lst = v
        return max(dp)
solu = Solution()
print(solu.longestValidParentheses("(()"))
