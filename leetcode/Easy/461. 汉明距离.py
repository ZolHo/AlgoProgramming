# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 7:36 下午
# @Author  : ZolHo.github.io
# @FileName: 461. 汉明距离.py

from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sx = '{:b}'.format(x)
        sy = '{:b}'.format(y)
        lx,ly = len(sx), len(sy)
        l = max(lx,ly)
        if lx > ly : sy = '0'*(lx-ly) + sy
        else : sx = '0' *(ly-lx) + sx
        # print(sx,sy)
        ans = 0
        for i in range(l):
            if sx[i]!=sy[i]: ans+=1
        return ans

solu = Solution()
print(solu.hammingDistance(1,4))
