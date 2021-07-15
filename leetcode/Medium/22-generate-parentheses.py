# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 11:06 上午
# @Author  : ZolHo
# @FileName: 22-generate-parentheses.py

class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def huisu(left, right, s):
            if (left<n):
                huisu(left+1, right, s+'(')
            if (right<left ):
                huisu(left, right+1, s+')')
            if (left == right == n) :
                ans.append(s)
        huisu(1,0,'(')

        return ans

solu = Solution()
print(solu.generateParenthesis(3))