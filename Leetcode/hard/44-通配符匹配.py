# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 9:35 下午
# @Author  : ZolHo.github.io
# @FileName: 44-通配符匹配.py

from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p :  return True
        if s and not p : return False
        mm = p[0]
        lst = mm
        for i in p[1:]:
            if not lst == i == '*': mm += i
            lst = i
        p = mm

        if not s and p != '*': return False
        dp = [[True for j in range(len(p))] for i in range(len(s))]

        def digui(i, j):
            # print(s[i:],p[j:],i,j)
            if not s[i:] and not p[j:]: return True
            if s[i:] and not p[j:] : return False
            if not s[i:] and p[j] != "*":
                return False
            if p[j:]=='*' : return True
            if s[i:]==p[j:] : return True

            pi = p[j]
            if pi == '*':
                for k in range(i,len(s) ):
                    if(dp[k][j+1]==0) :
                        # print("flagflag")
                        continue
                    if digui(k, j+1): return True
                    else : dp[k][j+1] = 0
                return False
            elif pi == '?':
                return digui(i+1, j+1)
            else:
                if pi != s[i]:
                    return False
                else:
                    return digui(i+1, j+1)
        return digui(0,0)


solu = Solution()
print(
    solu.isMatch("acdcb"
,"a*c?b"))
