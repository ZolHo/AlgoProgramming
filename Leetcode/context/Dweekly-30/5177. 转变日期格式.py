# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 10:27 下午
# @Author  : ZolHo.github.io
# @FileName: 5177. 转变日期格式.py

from typing import List
class Solution:
    def reformatDate(self, date: str) -> str:
        dts = date.split(" ")
        if len(dts[0])==4:
            day = dts[0][:2]
        else : day = '0'+str(dts[0][:1])
        moth = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":'06', "Jul":"07", "Aug":'08', "Sep":"09", "Oct":10, "Nov":11, "Dec":12}
        return str(dts[2])+'-'+str(moth[dts[1]])+'-'+str(day)

solu = Solution()
print(solu.reformatDate("20th Oct 2052"))
