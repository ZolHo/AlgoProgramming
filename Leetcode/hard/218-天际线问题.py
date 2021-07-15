# @time   :2021/07/13
# @author :ZolHo
# @file   :218-天际线问题.py

from typing import List

class ZoIntervalArr():
    def __init__(self):
        self.arr = []
    def add(self, left, right):
        arr = self.arr
        if len(arr) == 0 :
            arr.append((left, right))
            return [left]
        rs = None
        for i, temp in enumerate(arr) :
            if   left < temp[0] and right >= temp[0] :
                self.arr[i] = (left, max(temp[1], right))
                rs = [left]
            if left <= temp[1] and right > temp[1] :
                self.arr[i] = (min(left, temp[0]), right)
                rs = [temp[1]] if left >= temp[0] else [left, temp[1]]
            elif temp[0] <= left and temp[1] >= right :
                return []
            elif temp[0] > right or (i == len(arr)-1 and not rs):
                self.arr.append((left, right))
                rs = [left]
            if rs : break
        self.arr.sort()
        flag = True
        while flag :
            flag = False
            for i in range(len(self.arr)-1) :
                if self.arr[i][1] >= self.arr[i+1][0]:
                    flag = True
                    if self.arr[i][1] >= self.arr[i+1][1] : rs.append(arr[i+1][1])
                    self.arr[i] = (self.arr[i][0], max(self.arr[i][1], self.arr[i+1][1]))
                    self.arr.pop(i+1)
                    break
        return rs

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key= lambda x : x[2], reverse=True)
        zo, dotSet, ans = ZoIntervalArr(), set(), []
        for t in buildings:
            rs = zo.add(t[0], t[1])
            for r in rs :
                dotSet.add((r, t[2]))
        for t in zo.arr :
            dotSet.add((t[0], 0))
            dotSet.add((t[1],0))
        tempar = list(dotSet)
        tempar.sort()
        for i in range(1, len(tempar)) :
            if tempar[i][1] != tempar[i-1][1] : ans.append(list(tempar[i]))
        return ans


