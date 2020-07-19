# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:46 上午
# @Author  : ZolHo.github.io
# @FileName: 312. 戳气球.py

from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        jiyi = [[0]*len(nums) for i in range(len(nums))]
        for i in range(0,len(nums)-2):
            jiyi[i][i+2] = nums[i]*nums[i+1]*nums[i+2]
        print(nums,jiyi)
        def digui(i,j):
            if jiyi[i][j] !=0 : return jiyi[i][j]
            maxk,maxv = 0,0
            for k in range(i+1,j):
                tmp = nums[i]*nums[k]*nums[j] + digui(i,k) + digui(k,j)
                # print(k,tmp,i,j)
                if maxv <= tmp:
                    maxk, maxv = k,tmp
            # print(maxk)
            jiyi[i][j] = maxv
            return maxv
        digui(0, len(nums)-1)
        # print (jiyi)
        return jiyi[0][len(nums)-1]


solu = Solution()
print(solu.maxCoins([3,4]))
