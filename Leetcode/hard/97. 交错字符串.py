# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 1:14 上午
# @Author  : ZolHo.github.io
# @FileName: 97. 交错字符串.py

from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3) : return False
        if len(s1) == 0: return s2==s3
        if len(s2) == 0 : return s1==s3
        dp = [[-1 ] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0] = 1
        def digui(i,j,k):

            if (i<len(s1) and dp[i+1][j]!=-1) and (j<len(s2) and dp[i][j+1]!=-1): return
            if i<len(s1) and s1[i] == s3[k] :
                dp[i+1][j] = 1
                digui(i+1,j,k+1)
            elif i<len(s1) :
                dp[i+1][j] = 0
            if j<len(s2) and s2[j] == s3[k] :
                dp[i][j+1] = 1
                digui(i,j+1,k+1)
            elif j < len(s2):
                dp[i][j+1] = 0
        digui(0,0,0)
        return True if dp[len(s1)][len(s2)]==1 else False

solu = Solution()
print(solu.isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
,"abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
,"abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"))
