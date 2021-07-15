# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 11:11 上午
# @Author  : ZolHo.github.io
# @FileName: 5477. 排布二进制网格的最少交换次数


from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        gdlist = []
        chushilist = []
        for ii,i in enumerate(grid):
            tmp = 0
            for j in i[::-1] :
                if j==1:
                    gdlist.append((ii,tmp))
                    chushilist.append((ii,tmp))
                    break
                tmp+=1
            if tmp == len(grid):
                gdlist.append((ii, tmp))
                chushilist.append((ii, tmp))

        whatineed = [i for i in range(0,len(grid))[::-1]]
        gdlist.sort(key =lambda ele:(ele[1], ele[0]),reverse=True)
        for i in range(len(grid)):
            if gdlist[i][1]< whatineed[i]: return -1
        ans = 0
        for i in range(len(grid)):
            if chushilist[i][1] >= whatineed[i] : continue
            for j in range(i+1,len(grid)) :
                if chushilist[j][1] >= whatineed[i] :
                    ans += j-i
                    tt = chushilist.pop(j)
                    chushilist.insert(i,tt)
                    break
        return ans


solu = Solution()
print(solu.minSwaps([[0,0],[0,1]]))