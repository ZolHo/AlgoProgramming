# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 10:44 上午
# @Author  : ZolHo.github.io
# @FileName: 面试题 16.11. 跳水板.py

from typing import List

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k==0:return []
        tmp = shorter*k
        ans = [tmp]
        cha = longer-shorter
        if cha==0 : return ans
        for i in range (k):
            tmp += cha
            ans.append(tmp)
        return list(ans)
solu = Solution()
print(solu.divingBoard(2
,1118596
,979))
