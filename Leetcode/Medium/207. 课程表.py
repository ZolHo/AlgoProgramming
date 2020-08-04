# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 10:12 上午
# @Author  : ZolHo.github.io
# @FileName: 207. 课程表


from typing import List
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        linklist = [[] for i in range(numCourses)]
        for v in prerequisites:
            linklist[v[0]].append(v[1])
        isvisit = [False for i in range( numCourses)]
        def genxing() :
            hasnonext = [True for i in range(numCourses)]
            for i,v in enumerate(linklist):
                if v : hasnonext[i]  = False
            return [v for v in range(numCourses) if hasnonext[v] and not isvisit[v]]
        que = deque(genxing())
        for v in que: isvisit[v] = True
        while(que.__len__()):
            tmp = que.popleft()
            for v in linklist:
                if tmp in v :
                    v.remove(tmp)
            gx = genxing()
            for v in gx :
                que.append(v)
                isvisit[v] = True
        for v in isvisit:
            if not v : return False
        return True



solu = Solution()
print(solu.canFinish(2, [[1,0]]))