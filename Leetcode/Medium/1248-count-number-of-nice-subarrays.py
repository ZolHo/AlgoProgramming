# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:17 下午
# @Author  : ZolHo
# @FileName: 1248-count-number-of-nice-subarrays.py
class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        ans, newnums, odd = 0, [], 0
        for x in nums:
            if (x%2==0) :
                odd+=1
            else:
                newnums.append(odd)
                newnums.append(-1)
                odd = 0
        newnums.append(odd)

        # for x in newnums:
        #     print(x, end=" ")

        if (len(newnums)//2<k):
            return 0

        for x in range(len(newnums))[1::2]:
            if (x+2*(k-1)<len(newnums)) :
                ans += (newnums[x-1]+1)*(newnums[x+2*(k-1)+1]+1)
            else:
                break

        return ans;

#执行用时 :1080 ms, 在所有 Python3 提交中击败了53.17%的用户
#内存消耗 :20.5 MB, 在所有 Python3 提交中击败了25.00%的用户

solu = Solution()
ans = solu.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2)
print(ans)