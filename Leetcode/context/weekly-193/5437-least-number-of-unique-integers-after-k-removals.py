# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 10:54 上午
# @Author  : ZolHo
# @FileName: 5437-least-number-of-unique-integers-after-k-removals.py

from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cont = Counter(arr)
        for v in cont.most_common()[::-1]:
            if (v[1]<=k):
                cont[v[0]] = 0
                k -= v[1]
            else:
                break
        return (len(+cont))

        # for i in di.keys():
        #     ar.append((i,di[i]))
        # ar.sort(key =lambda ele:(ele[1],ele[0]))
        # for v in ar:
        #     if (v[1]<=k):
        #         print(v[0])
        #         di.pop(v[0])
        #         k -= v[1]
        #     else :
        #         break

solu = Solution()
print(solu.findLeastNumOfUniqueInts([5,5,4],1))