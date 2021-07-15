# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 9:17 上午
# @Author  : ZolHo
# @FileName: 14-最长公共前缀和.py

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans, flag = "", False
        if (len(strs) <= 0):
            return ""
        dimin = len(strs[0])
        for v in strs:
            dimin = min(dimin, len(v))

        for i in range(dimin):
            temp = strs[0][i]
            for v in strs[1:]:
                if (v[i]!=temp):
                    flag = True
                    break
            if (flag) :
                break
            ans += temp
        return ans


solu = Solution()
print(solu.longestCommonPrefix(["abca","abc"]))