# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 12:35 下午
# @Author  : ZolHo.github.io
# @FileName: 5442-避免洪水泛滥.py

from typing import List

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
                        for i,v in enumerate(rains[tmp[0]:]):
                            if(v==tmp[1]):
                                firstday[tmp[1]] = tmp[0]+i
                                break
                        break
                if(not flag) :
                    ans.append(1)
            else:
                ans.append(-1)
        print(q, ans)
        if (len(q)>0) : return []
        return ans

solu = Solution()
print(solu)
