# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:20 下午
# @Author  : ZolHo.github.io
# @FileName: 67-二进制求和.py

from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(a[0]=='0' or b[0]=='0') : return a if(b[0]=='0') else b
        if (len(b)>len(a)) : a,b = b,a
        la, lb = len(a), len(b)
        tmp, ans = 0, ''
        for i in range(lb):
            sums = int(a[-1-i]) + int(b[-1-i]) + tmp
            if (sums==3) : tmp, ans = 1, '1' + ans
            elif (sums==2) : tmp, ans = 1, '0' + ans
            elif (sums==1) : tmp, ans = 0, '1' + ans
            else : tmp, ans = 0, '0' + ans
        i += 1
        while(tmp==1 and i <la ) :
            sums = tmp + int(a[-1-i])
            if (sums==2) : tmp, ans = 1, '0' + ans
            elif (sums==1) : tmp, ans = 0, '1' + ans
            i+=1
        return (a[:-i] + ans) if (tmp==0) else ('1' + a[:-i] + ans)
solu = Solution()
print(solu)
