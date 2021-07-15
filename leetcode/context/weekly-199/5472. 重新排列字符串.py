# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 12:01 下午
# @Author  : ZolHo.github.io
# @FileName: 5472. 重新排列字符串


from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ns = [0 for i in s]
        for i,v in enumerate(indices):
            ns[v] = s[i]
        ans = ''
        for v in ns:
            ans+=v
        return ans
solu = Solution()
print(solu)