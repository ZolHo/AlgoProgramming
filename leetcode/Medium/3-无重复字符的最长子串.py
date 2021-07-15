# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 6:17 下午
# @Author  : ZolHo.github.io
# @FileName: 3-无重复字符的最长子串.py

from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (not s) : return 0
        lst = [(v,i) for i, v in enumerate(s)]
        dp = [1,]
        for v in lst[1:]:
            k = -1
            for y in lst[v[1]-dp[v[1]-1]:v[1]]:
                if (y[0]==v[0]) :
                    k = y[1]
                    break
            if (k!=-1) : dp.append( v[1] - k )
            else : dp.append(dp[v[1]-1]+1)
        return max(dp)


solu = Solution()
print(solu.lengthOfLongestSubstring("pwwkew"))