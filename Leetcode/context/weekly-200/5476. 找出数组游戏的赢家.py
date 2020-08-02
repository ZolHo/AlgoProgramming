# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 11:02 上午
# @Author  : ZolHo.github.io
# @FileName: 5476. 找出数组游戏的赢家


from typing import List
from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        lianwin = 0
        arr = deque(arr)
        if k >= len(arr) : return max(arr)#特判，举报吧
        while(lianwin<k) :
            a0 = arr.popleft()
            a1 = arr.popleft()
            if a0 > a1 :
                lianwin+=1
                arr.appendleft(a0)
                arr.append(a1)
            else:
                lianwin = 1
                arr.appendleft(a1)
                arr.append(a0)
        return arr[0]
solu = Solution()
print(solu)