# @time   :2021/07/18
# @author :ZolHo
# @file   :3.py

from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for i in range(1,len(points)):
            tem = [(points[i][j],j) for j in range(len(points[0]))]
            tem.sort(key=lambda x:x[0],reverse=True)
            for j in tem[:5]:
                m = j[0] + points[i-1][j[1]]
                for k in range(len(points[0])) :
                    # if points[i-1][k]+points[i][j[1]] < m :continue
                    m = max (m, points[i-1][k]+j[0] -abs (k-j[1]))
                points[i][j[1]] = m
        return max(points[-1])


