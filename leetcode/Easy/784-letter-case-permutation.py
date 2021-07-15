# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 11:08 上午
# @Author  : ZolHo
# @FileName: 784-letter-case-permutation.py

class Solution:#dfs
    def letterCasePermutation(self, S: str):
        ans, str = [], S.lower()
        def dfs(i,s):
            if (i>= len(str)):
                ans.append(s)
                return
            if (str[i].isdigit()):
                dfs(i+1,s+str[i])
            else:
                dfs(i+1, s+str[i])
                dfs(i+1, s+str[i].upper())
        dfs(0,"")
        return ans

#执行用时 :80 ms, 在所有 Python3 提交中击败了44.19%的用户
#内存消耗 :15.1 MB, 在所有 Python3 提交中击败了100.00%的用户
solu = Solution()
print(solu.letterCasePermutation("a1b2"))