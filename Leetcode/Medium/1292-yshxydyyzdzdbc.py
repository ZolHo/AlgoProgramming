# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 9:52 上午
# @Author  : ZolHo
# @FileName: 1292-yshxydyyzdzdbc.py

class Solution:#不看清题，绕一大圈
    def maxSideLength(self, mat, threshold: int) -> int:
        qzh = [[0 for y in range(len(mat[0])+1)] for x in range(len(mat)+1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                qzh[i][j] = mat[i][j]+qzh[i-1][j]+qzh[i][j-1]-qzh[i-1][j-1]
        max_len = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for k in range(max_len+1,max(len(mat),len(mat[0]))):
                    if (i+k>=len(mat) or j+k>=len(mat[0])):
                        break
                    q_sum = qzh[i+k][j+k]-qzh[i-1][j+k]-qzh[i+k][j-1]+qzh[i-1][j-1]
                    if (q_sum>threshold):
                        break
                    else:
                        max_len = k
        return max_len if (max_len==0) else max_len+1

solu = Solution()
print(solu.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4))