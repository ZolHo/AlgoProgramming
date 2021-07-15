from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def numsort(x, y) :
            print(x+y,y+x)
            return -1 if x+y >y+x else 1

        strnums = [str(i) for i in nums]
        strnums.sort(key=functools.cmp_to_key(numsort))
        ans = "".join(strnums)
        ans = ans.lstrip("0")
        return ans if ans!="" else "0"
so = Solution()
print(so.largestNumber([111311,1113]))