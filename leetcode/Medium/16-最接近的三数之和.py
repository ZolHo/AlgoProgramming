# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 11:31 上午
# @Author  : ZolHo.github.io
# @FileName: 16-最接近的三数之和.py

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = sum(nums[:3])
        nums = sorted(nums)
        for i, iv in enumerate(nums):
            for j in range(i + 1, len(nums) - 1):
                lastcha = abs(target - iv - nums[j] - nums[j + 1])
                if (abs(ans - target) > lastcha): ans = iv + nums[j] + nums[j + 1]
                for k in range(j + 1, len(nums)):
                    cha = abs(target - iv - nums[j] - nums[k])
                    if (cha > lastcha): break
                    if (cha < abs(ans - target)): ans = iv + nums[j] + nums[k]
                    lastcha = cha

        return ans
solu = Solution()
print(solu)
