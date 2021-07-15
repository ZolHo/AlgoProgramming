from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid, lt, rt = len(nums)//2, 0, len(nums)
        while rt > lt:
            # print(lt,mid,rt)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[lt] :
                if target > nums[mid]:
                    lt = mid+1
                else:
                    if target >= nums[lt]:
                        rt = mid
                    else:
                        lt = mid+1
                mid = (rt + lt) // 2
            else:
                if target > nums[mid] :
                    if target >= nums[lt] :
                        rt = mid
                    else:
                        lt = mid +1
                else:
                    rt = mid
                mid = (rt+lt) //2
        return -1

so = Solution()
print(so.search([1],
0))