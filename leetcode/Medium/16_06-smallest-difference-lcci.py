# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 6:46 下午
# @Author  : ZolHo
# @FileName: 16_06-smallest-difference-lcci.py

class Solution:
    def smallestDifference(self, a, b) -> int:
        a.sort(), b.sort()
        ans = abs(a[0]-b[0])
        k = max (a[0], b[0])

        if (a[0]>b[0]):
            a,b = b,a

        # if (a[len(a)-1]<b[0]):
        #     return
        i, j = 0, 0
        while(i<len(a) and j <len(b)) :
            print(i,j)
            while(i<len(a) and j <len(b) and a[i]<=b[j] ) :
                ans = min(abs(a[i]-b[j]),ans)
                i += 1
            while(i<len(a) and j <len(b) and b[j]<a[i] ) :
                ans = min (abs(a[i]-b[j]),ans)
                j += 1

        return ans

#执行用时 :264 ms, 在所有 Python3 提交中击败了54.75%的用户
#内存消耗 :19.6 MB, 在所有 Python3 提交中击败了100.00%的用户
solu = Solution()
ans = solu.smallestDifference([1,2,11,15],[4,12,19,23,127,11])
print(ans)