# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 3:09 下午
# @Author  : ZolHo.github.io
# @FileName: 18-四数之和


from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        iset = set()
        if len(nums)<=3: return ans
        zidian = {}
        for i, iv in enumerate(nums):
            zidian[iv] = i
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    if (nums[i], nums[j], nums[k]) in iset : continue
                    temp = target-(nums[i]+nums[j] +nums[k])
                    if temp in zidian.keys() and zidian[temp] > k:
                        ans.append([nums[i], nums[j], nums[k], nums[zidian[temp]]])
                        iset.add((nums[i], nums[j], nums[k]))
        return ans

solu = Solution()
print(solu.fourSum([1,0,-1,0,-2,2]
,0))