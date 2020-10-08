# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 9:40 上午
# @Author  : ZolHo.github.io
# @FileName: 75.颜色分类


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, now = 0, len(nums) - 1, 0
        while (now <= right and now >= left):
            if nums[now] == 0:
                nums[now], nums[left] = nums[left], nums[now]
                if now == left: now += 1
                left += 1
            elif nums[now] == 2:
                nums[now], nums[right] = nums[right], nums[now]
                right -= 1
            else:
                now += 1
        return nums


solu = Solution()
print(solu)