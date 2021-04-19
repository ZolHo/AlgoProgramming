from typing import List
from functools import reduce
import operator

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        def get_i(x, i) :
            return (x>>i) & 1
        temp = [0 for i in range(32)]
        temp2 = [0 for i in range(32)]
        for i in range(32):
            for x in arr1:
                temp[i] += get_i(x,i)
            for y in arr2:
                temp2[i] += get_i(y,i)
            t = temp[i] *temp2[i]
            # print(temp[i], temp2[i],t, t&1)
            if t&1==1:

                ans|=1<<i
        return ans






so = Solution()
print(so.getXORSum([12],[4]))