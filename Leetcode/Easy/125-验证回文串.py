# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 10:24 上午
# @Author  : ZolHo.github.io
# @FileName: 125-验证回文串.py

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (s=='') : return True
        s = s.lower()
        ans = ''
        for v in s: ans += v if (v in '1234567890qwertyuiopasdfghjklzxcvbnm') else ''
        return ans == ans[::-1]

