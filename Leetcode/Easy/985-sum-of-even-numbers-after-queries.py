# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 9:56 上午
# @Author  : ZolHo
# @FileName: 985-sum-of-even-numbers-after-queries.py

from typing import List
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        a_sum, ans = 0, [0 for i in range(len(queries))]
        for v in A:
            if (v%2==0) :
                a_sum += v
        for i in range(len(queries)):
            index, value = queries[i][1], queries[i][0]
            if (A[index]%2==0 and value%2==0) :
                ans[i] = a_sum+value
            if (A[index]%2==0 and value%2!=0) :
                ans[i] = a_sum - A[index]
            if (A[index] % 2 != 0 and value % 2 != 0):
                ans[i] = a_sum + A[index] +value
            if (A[index] % 2 != 0 and value % 2 == 0):
                ans[i] = a_sum
            A[index] += value
            a_sum = ans[i]
        return ans

solu = Solution()
print(solu.sumEvenAfterQueries([3,2]
,[[4,0],[3,0]]))