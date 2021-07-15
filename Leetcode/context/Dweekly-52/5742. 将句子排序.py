from typing import List
from functools import reduce
import operator

class Solution:
    def sortSentence(self, s: str) -> str:
        ar = s.split(" ")
        d = dict()
        for i in ar :
            for j in range(len(i)-1):
                if i[j] in "0123456789" :
                    break
            d[int(i[j+1:])] = i[:j+1]
        b = []
        for i in range(len(ar)) :
            b.append(d[i+1])
        return " ".join(b)
