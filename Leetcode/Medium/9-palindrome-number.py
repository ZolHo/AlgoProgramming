# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 10:55 上午
# @Author  : ZolHo
# @FileName: 9-palindrome-number.py

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        else:
            x = str(x)
            return x==x[::-1]

solu = Solution()
print(solu.isPalindrome(121))
