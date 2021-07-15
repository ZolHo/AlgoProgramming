from typing import List
from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        temp = "".join(words)
        c = Counter(temp)
        m = len(words)
        if m == 1 : return True
        tt = 0
        for k in c:
            if c[k] % m != 0:
                return False
            else :
                tt += c[k]//m
        return tt ==len(temp)//m
