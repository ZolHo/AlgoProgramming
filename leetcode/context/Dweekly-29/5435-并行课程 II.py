# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 11:43 下午
# @Author  : ZolHo.github.io
# @FileName: 5435-并行课程 II.py

from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        mp = [False for i in range(n+1)]
        mp[0] = True
        term = 0
        while (True):
            frontm = set([])
            fsb = set([])
            for v in dependencies:
                fsb.add(v[0])
                if(mp[v[0]]==False) : frontm.add(v[1])
            backm = [p for p in range(1,n+1) if p not in frontm and not mp[p]]

            fsb = fsb & set(backm)
            ttk = 0
            for i in range(len(backm)):
                if(backm[i] in fsb):
                    backm[i], backm[ttk] = backm[ttk], backm[i]
                    ttk += 1

            if(len(backm)<=k):
                # print(len(backm), k)
                for s in backm:
                    mp[s] = True
                term+=1
            else:
                tmp1 = len(backm)//k
                term += tmp1
                for i in range(tmp1*k):
                    mp[backm[i]] = True
            # print(frontm,backm,mp)
            fl = True
            for i in mp:
                if(not i) : fl = False
            if(fl) : break
        return term