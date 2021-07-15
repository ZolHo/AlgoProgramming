from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        lenth = len(nums)
        if lenth <=3 :
            return max(nums)
        dpleft = [[0 for j in range(lenth-1)] for i in range (lenth//2+20)]
        dpright = [[0 for j in range(lenth-1)] for i in range(lenth//2+20)]
        dpleft[0][0], dpright[0][0] = nums[0], nums[1]
        for i in range(1, lenth-1):
            dpleft[0][i], dpright[0][i] = max(nums[:i+1]), max(nums[1:i+2])
        for i in range(1, lenth//2+20) :
            dpleft[i][0], dpleft[i][1], dpright[i][0], dpright[i][1] = nums[0], max(nums[0], nums[1]), nums[1],max(nums[2], nums[1])
        for i in range(1, lenth//2+20) :
            for j in range(2, lenth-1) :
                dpleft[i][j] = max(dpleft[i-1][j-2]+nums[j], dpleft[i-1][j-1])
                dpright[i][j] = max(dpright[i-1][j-2] + nums[j+1], dpright[i-1][j-1])
        print(dpleft)
        print()
        print(dpright)
        return max(dpleft[-1][-1], dpright[-1][-1])


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         sum, ans, count = 0, 0, 0
#         is_visit = [False for i in range(len(nums))]
#         houzhuihe = [0 for i in range(len(nums))]
#         houzhuihe[-1] = nums[-1]
#         for i in range(len(nums)-1)[::-1]:
#             houzhuihe[i] = houzhuihe[i+1] + nums[i]
#         def shengsou(depth) :
#             nonlocal sum, ans, count
#             count += 1
#             lenth = len(is_visit)
#
#             if depth >= lenth or sum + houzhuihe[depth] < ans :
#                 return
#
#             for i in range(depth, lenth):
#                 if not is_visit[i]:
#                     is_visit[i] = True
#                     ltemp, rtemp = is_visit[(i+lenth-1)%lenth], is_visit[(i+1)%lenth]
#                     is_visit[(i + lenth - 1) % lenth], is_visit[(i + 1) % lenth] = True, True
#                     sum+=nums[i]
#                     if sum > ans :
#                         ans = sum
#                     shengsou(i+2)
#                     sum -= nums[i]
#                     is_visit[(i + lenth - 1) % lenth], is_visit[(i + 1) % lenth] = ltemp, rtemp
#                     is_visit[i] = False
#         shengsou(0)
#         print(count)
#         return ans

solu = Solution()
print(solu.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))