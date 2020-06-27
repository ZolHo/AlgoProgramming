# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 11:39 下午
# @Author  : ZolHo.github.io
# @FileName: 5432-去掉最低工资和最高工资后的工资平均值.py

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        a = sum(salary)
        a = a - max(salary)-min(salary)
        return a/(len(salary)-2)