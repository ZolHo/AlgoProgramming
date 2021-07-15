# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 4:03 下午
# @Author  : ZolHo.github.io
# @FileName: 7-整数反转.py

from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1] if (x>=0) else ("-"+str(x)[::-1])[:-1]
        return 0 if ( len(s)>11 or int(s)>2147483647 or int(s)<-2147483648) else int(s)