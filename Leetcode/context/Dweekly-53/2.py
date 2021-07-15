from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        lo, hi = nums[0]+nums[1], nums[-1] + nums[-2]
        mid = (lo+hi)//2
        tmap = {}
        t = 0
        for i in range(min(nums), max(nums)+1) :
            if i > nums[t] : t+=1
            tmap[i] = min(len(nums)-1,t)

        while lo < hi :
            flag = True
            isv = [False for i in range(len(nums))]
            for i in range(len(nums)) :
                if mid-nums[i] < nums[0] : break
                ik = False
                for j in range(i+1, len(nums))[::-1] :
                    if mid -nums[i] >= nums[j] and not isv[i] and not isv[j]:
                        isv[i] , isv[j],ik = True, True, True
                        break
                if not ik : break
            for i in range(len(nums)) :
                if isv[i] == False:
                    flag = False
            if flag:
                hi = mid
            else:
                lo = mid+1
            mid = (lo+hi)//2

        return lo