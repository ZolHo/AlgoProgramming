# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 10:58 上午
# @Author  : ZolHo.github.io
# @FileName: dier


from typing import List
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        if n==1:return '0'
        lenth = 1
        for i in range(n-1):
            if lenth >= k  : break
            lenth = lenth*2+1
        n = i+1
        for i in range(n):
            tmp = s
            s+='1'
            new = ''
            for pp,j in enumerate(tmp):
                new += str(1-int(j))


            s+=new[::-1]
            # print()
        print(s,k)
        return s[k-1]



solu = Solution()
print(solu.findKthBit(3,1))