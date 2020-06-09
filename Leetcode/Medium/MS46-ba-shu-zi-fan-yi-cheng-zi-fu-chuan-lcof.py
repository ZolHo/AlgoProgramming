# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 7:37 上午
# @Author  : ZolHo
# @FileName: MS46-ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof.py

class Solution:
    def translateNum(self, num: int) -> int:
        ## dp

        s = str(num)
        dp = [0 for x in range(0,len(s)+1)]
        dp[0], dp[1] = 1, 1
        for i in range(1,len(s)):
            print(s[i:i+2])
            if (i+1<=len(s) and s[i-1]!='0' and int(s[i-1:i+1])<=25) :
                dp[i+1] = dp[i]+dp[i-1]
            else:
                dp[i+1] = dp[i]
        # print (dp)
        return dp[len(s)]

        ## DFS

        # ans, s = 0, str(num)
        # def dfs(i):
        #     if (i>= len(s)):
        #         nonlocal ans
        #         ans += 1
        #         return
        #
        #     dfs(i+1)
        #     if (i+1<len(s) and s[i]!='0' and int(s[i:i+2])<=25):
        #         dfs(i+2)
        # dfs(0)
        # return ans

#执行用时 :36 ms, 在所有 Python3 提交中击败了83.43%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了100.00%

solu = Solution()
print(solu.translateNum(25))
