# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 10:07 上午
# @Author  : ZolHo.github.io
# @FileName: first


from typing import List

class Solution:
    def makeGood(self, s: str) -> str:
        lst = ""
        while s!=lst:
            bolll = [True for i in s]
            for i in range(0, len(s)-1):
                if s[i] == s[i].lower() and bolll[i] and bolll[i+1] and s[i].lower()==s[i+1].lower():
                    if s[i+1] ==s[i+1].upper():
                        bolll[i] = False
                        bolll[i+1] = False
            for i in range(0, len(s)-1):
                if s[i] == s[i].upper() and bolll[i] and bolll[i+1] and s[i].lower()==s[i+1].lower():
                    if s[i+1] ==s[i+1].lower():
                        bolll[i] = False
                        bolll[i+1] = False
            tmp = ''
            for i,v in enumerate(bolll):
                if v:
                    tmp+=s[i]
            lst = s
            s = tmp

        return s



solu = Solution()
print(solu.makeGood("abBAcC"))