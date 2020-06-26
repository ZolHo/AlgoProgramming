# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 11:02 上午
# @Author  : ZolHo
# @FileName: test.py

from array import array
from typing import List
from collections import deque

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        q = []
        tm = set([])
        firstday = {}
        ans = []
        for i,v in enumerate(rains):
            if (v in tm and v!=0):
                q.append((i,v))
            else:
                tm.add(v)
                if(v!=0):firstday[v] = i
        print(q)
        print(firstday)
        for i,v in enumerate(rains):
            if (v == 0) :
                if (len(q)==0) :
                    ans.append(1)
                    continue
                # tmp = q.popleft()
                flag = False
                for j,tmp in enumerate(q):
                    if(i<tmp[0] and i>firstday[tmp[1]]) :
                        flag = True
                        ans.append(tmp[1])
                        q.pop(j)
                if(not flag) :
                    ans.append(1)
            else:
                ans.append(-1)
        print(q, ans)
        if (len(q)>0) : return []
        return ans

solu = Solution()
print(solu.avoidFlood([1,0,2,0,2,1]))

