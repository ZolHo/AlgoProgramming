from typing import List
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        for i in range(1,min(len(grid[0]),len(grid)))[::2]:
            print(i)