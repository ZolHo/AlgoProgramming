# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 9:49 上午
# @Author  : ZolHo.github.io
# @FileName: 面试题 17.13. 恢复空格.py

from typing import List

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if len(sentence) <= 0: return 0
        if len(dictionary) <= 0: return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]

solu = Solution()
print(solu)
