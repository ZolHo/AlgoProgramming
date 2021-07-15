# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 12:32 上午
# @Author  : ZolHo
# @FileName: 15-3sum.py

class Solution:#气死啦，晚上喝了点酒来写题，continue全写成了break，改了好多次
    def threeSum(self, nums) :
        ans, dic_num, nums = [], {}, sorted(nums)
        for x in nums:
            if (x in dic_num.keys()):
                dic_num[x] += 1
            else:
                dic_num[x] = 1
        for i,x in enumerate(nums):
            if (x > 0 or (i>0 and x==nums[i-1])):
                continue
            dic_num[x] -= 1
            tmp = nums[i+1:len(nums)]
            for j,y in enumerate(tmp):
                if(y+x>0 or (j>0 and y==tmp[j-1]) or 0-x-y < y):
                    continue
                dic_num[y] -= 1
                if (x==y==0 and dic_num[0]>=1):
                    ans.append([0,0,0])
                if (0-x-y>0 and 0-x-y in dic_num.keys() and dic_num[0-x-y]>=1):
                    ans.append([x,y,0-x-y])
                dic_num[y]+=1
            dic_num[x]+=1
        return ans

solu = Solution()
print(solu.threeSum([0,-4,-1,-4,-2,-3,2]))