from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in costs:
            if coins >= i :
                coins -= i
                ans +=1
            else:
                break
        return ans

so = Solution()
print(so.maxIceCream([1,3,2,4,1],
7))