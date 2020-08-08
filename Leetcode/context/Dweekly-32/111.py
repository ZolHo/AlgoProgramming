# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 9:34 下午
# @Author  : ZolHo.github.io
# @FileName: 111


from typing import List
from collections import Counter
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        thealap = 'abcdefghijklmnopqrstuvwxyz'
        dt = {}
        for i,v in enumerate(thealap):
            dt[v] = i+1
        lianbiao = [[] for i in range(len(s))]
        isvisit = [True for i in range(len(s))]
        sst = set([])
        for i in range(len(s)):
            if s[i] != t[i]:
                isvisit[i] = False
                jieguo = dt[t[i]] - dt[s[i]]
                if jieguo<0 : jieguo+=26
                while jieguo <= k:
                    lianbiao[i].append(jieguo)
                    sst.add(jieguo)
                    jieguo+=26
        setdt = {}
        for i in sst:
            setdt[i] = False
        tmp = 0
        for i in lianbiao:
            if i: tmp += 1
        if tmp > sst.__len__():
            return False
        print(lianbiao)
        flag = False
        cishu = []
        for i in lianbiao:
            if not i:
                for j in i:
                    cishu.append(j)
        cishudt = Counter(cishu)
        for inex, i in enumerate(lianbiao):
            if not i:
                for j in i:
                    if cishudt[j] == 1: isvisit[inex] = True
        def digui(star):
            nonlocal flag, isvisit,sst
            if flag : return
            tpp  = True
            # print(isvisit)
            for i in isvisit :
                if not i : tpp = False
            if tpp :
                flag = True

            print(star)
            for i in range(star, len(s)):
                if not isvisit[i] :
                    for j in lianbiao[i]:
                        if not setdt[j] :
                            isvisit[i] = True
                            setdt[j] = True
                            digui(i+1)
                            isvisit[i] =False
                            setdt[j] = False
        digui(0)
        if flag : return True
        else: return False



solu = Solution()
print(solu.canConvertString("khduaokbwarmpvlji"
,"kyqwszryfonixjefm"
,70))