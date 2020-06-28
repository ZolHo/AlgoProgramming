# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 1:48 下午
# @Author  : ZolHo.github.io
# @FileName: 5449-检查数组对是否可以被 k 整除.py

from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if (sum(arr) % k != 0): return False
        mp = [0 for i in range(k)]
        for v in arr:
            mp[v%k] +=1
        if(mp[0]%2!=0) : return False
        for i, v in enumerate(mp):
            ned = (k-i)%k
            if(mp[ned]!=v) : return False
        return True
