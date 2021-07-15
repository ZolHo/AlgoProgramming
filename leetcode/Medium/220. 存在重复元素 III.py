from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ns = [0 for i in range(len(nums))]
        for i in range(len(nums)) :
            ns[i] = (nums[i], i)
        ns.sort()
        for i in range(len(nums)) :
            for j in range(i+1, len(nums)):
                if abs(ns[i][0] - ns[j][0]) <= t:
                    if abs(ns[i][1] -ns[j][1]) <= k:
                        return True
                else:
                    break
        # print(ns)
        return False
