# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 12:31 下午
# @Author  : ZolHo.github.io
# @FileName: 5441-保证文件名唯一.py
from typing import List
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        p = {}
        ans = []
        for i in names:
            if(i not in p.keys()) :
                ans.append(i)
                p[i] = 0
            else:
                k = p[i]+1
                tmp = i + '(' + str(k) + ")"
                while(True):
                    if(tmp in p.keys()) :
                        k +=1
                        tmp = i + '(' + str(k) + ")"
                    else:
                        p[i] = k
                        p[tmp] = 0
                        ans.append(tmp)
                        break
        return ans