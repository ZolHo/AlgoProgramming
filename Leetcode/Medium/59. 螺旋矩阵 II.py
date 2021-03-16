from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[1 for i in range(n)] for j in range(n)]
        def digui(M,deep,lenth, N) :
            temp = N
            if lenth < 1:
                return
            for i in range(lenth):
                M[deep][deep+i] = temp
                temp+=1
            for i in range(1,lenth):
                M[deep+i][deep+lenth-1] = temp
                temp += 1
            for i in range(lenth-1)[::-1]:
                M[deep+lenth-1][deep+i] = temp
                temp += 1
            for i in range(1,lenth-1)[::-1]:
                M[deep+i][deep] = temp
                temp += 1
            digui(M, deep+1, lenth-2, temp)
        digui(mat, 0, n,1)
        return mat

solu = Solution()
solu.generateMatrix(2)