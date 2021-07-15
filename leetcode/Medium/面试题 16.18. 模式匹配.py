# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 11:50 上午
# @Author  : ZolHo.github.io
# @FileName: 面试题 16.18. 模式匹配.py

from typing import List


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if (len(pattern) == 1): return True
        if (len(pattern) == 0 and len(value) == 0): return True
        if (len(pattern) == 0 or len(value) == 0): return False
        re = False if (pattern[0] == 'a') else True
        na, nb = pattern.count('a'), pattern.count('b')
        if (re): na, nb = nb, na
        if (na == 0 or nb == 0): return True if (len(value) % max(na, nb) == 0 and max(na, nb) == value.count(
            value[:len(value) // max(na, nb)])) else False

        for i in range(len(value) // na + 1):
            ter = len(value) - na * i
            if (ter % nb != 0): continue
            sa = value[:i]
            if (re):
                indx = pattern.find('a')
            else:
                indx = pattern.find('b')
            sb = value[indx * i:indx * i + ter // nb]
            c = sa
            print(sa, sb)
            if (sa == sb): continue
            for j in pattern[1:]:
                if (j == pattern[0]):
                    c += sa
                else:
                    c += sb
            if (c == value): return True
        return False

