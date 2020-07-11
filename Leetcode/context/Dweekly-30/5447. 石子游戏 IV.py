# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 10:27 下午
# @Author  : ZolHo.github.io
# @FileName: 5447. 石子游戏 IV.py

from typing import List
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        iswin = [0]*(n+1)
        iswin[n] = 1
        pf = []
        i = 1
        while i*i<=n:
            pf.append(i*i)
            i+=1
        for i in pf:
            m = n - i
            if 0<m:iswin[m] = -1
            else:break

        for sb in range(1,n)[::-1]:
            if iswin[sb]==-1:
                for i in pf:
                    m = sb - i
                    if 0 < m<sb:
                        if iswin[m]!=0:continue
                        iswin[m] = 1
                    else:
                        break
            else:
                for i in pf:
                    m = sb - i
                    if 0 < m<sb  :
                        iswin[m] = -1
                    else:
                        break
        # print(iswin)
        for i in pf :
            if i < len(iswin):
                if iswin[i] == 1: return True
        return False
solu = Solution()
print(solu.winnerSquareGame(8))
