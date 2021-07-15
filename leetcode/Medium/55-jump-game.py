# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 9:21 上午
# @Author  : ZolHo
# @FileName: 55-jump-game.py

class Solution:#广搜剪枝
    def canJump(self, nums) -> bool:
        rightest= 0
        for i, num in enumerate(nums):
            if (i<=rightest):
                rightest = max(rightest, i+num)
        return rightest>=len(nums)-1

        # isvisit = [False for x in range(len(nums))]
        # queue, isvisit[0], leftest = [0], True, 1
        # while(len(queue)>0):
        #     if (isvisit[len(nums)-1]):
        #         break
        #     temp = queue.pop()
        #     step = nums[temp]
        #     left, right = temp-step, temp+step+1
        #     if (left<leftest):
        #         left = leftest
        #     if (right>=len(nums)):
        #         right = len(nums)
        #     print(left, right)
        #     for i in range(left, right):
        #         if (i<0 or i>=len(nums) or isvisit[i]==True):
        #             continue
        #         if (leftest+1==i):
        #             leftest += 1
        #         isvisit[i] = True
        #         queue.append(i)
        #
        # return isvisit[len(nums)-1]

#执行用时 :48 ms, 在所有 Python3 提交中击败了81.13%的用户
#内存消耗 :15.2 MB, 在所有 Python3 提交中击败了6.90%的用户
solu = Solution()
print(solu.canJump([0]))