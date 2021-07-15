from typing import List

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        ans = 0
        while sum(diff) :
            idx_max = 0
            for i in range(len(nums1)):
                if diff[i] > diff[idx_max]:
                    idx_max = i
            idx_min = idx_max
            for i in range(len(nums1)):
                if abs(nums1[i]-nums2[idx_max]) < abs(nums1[idx_min] - nums2[idx_max]):
                    idx_min = i
            diff[idx_max] = abs(nums1[idx_min]- nums2[idx_max])
            # print(idx_max, idx_min)
            if idx_min == idx_max:
                ans += diff[idx_max]
                diff[idx_max] = 0
            else :
                break
        return sum(diff,ans)%1000000007


so = Solution()
print(so.minAbsoluteSumDiff([1,28,21],[9,21,20]))