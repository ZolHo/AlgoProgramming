from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        hangqianzhui = [[grid[_][0]] * len(grid[0])+[0] for _ in range(len(grid))]
        lieqianzhui = [[0]*len(grid[0])  for _ in range(len(grid)+1)]
        lieqianzhui[0] = grid[0]
        h, w = len(grid), len(grid[0])
        for i in range(h) :
            for j in range(1,w) :
                hangqianzhui[i][j] = hangqianzhui[i][j-1] + grid[i][j]
        for j in range( w):
            for i in range(1,h) :
                lieqianzhui[i][j] = lieqianzhui[i-1][j] + grid[i][j]
        # print(hangqianzhui)
        # print(lieqianzhui)
        def panduan (i,j,t) :
            flag = True
            hang = hangqianzhui[i][j+t] - hangqianzhui[i][j-1]
            lie = lieqianzhui[i+t][j] - lieqianzhui[i-1][j]
            if hang != lie : return False
            for t0 in range(i+1,i+t+1) :
                if hangqianzhui[t0][j+t] - hangqianzhui[t0][j-1] != hang : flag = False
            for t1 in range(j+1, j+t+1) :
                if lieqianzhui[i+t][t1] - lieqianzhui[i-1][t1] != lie : flag = False
            su1, su2 = 0, 0
            for t0 in range(i, i+t+1) :
                su1 += grid[t0][j+t0-i]
                su2 += grid[t0][j+i+t-t0]
            if su1!=su2 or su1!= hang :
                flag = False
            # print(i,j,t,hang,lie,su1,su2)
            return flag
        tim = min(h,w)
        for t in range(1,tim)[::-1] :
            for i in range(h-t) :
                for j in range(w-t) :
                    if panduan(i,j, t) :
                        return t+1
        return 1


